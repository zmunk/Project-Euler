import numpy as np
from math import log, ceil

BIG = np.uint32
SMALL = np.uint16

class Primer:
    ''' Class for generating primes '''
    def primes_until(self, num):
        ''' returns list of primes less than or equal to num '''
        try:
            self.primes = np.loadtxt(f'primesuntil{num}.txt', dtype=int)
            return self.primes
        except IOError:
            pass

        self.n = num
        self.flags = np.ones((self.n + 1,), dtype=bool)
        self.flags[[0,1]] = 0  # remove 0 and 1
        
        num_of_primes = ceil(1.7 * num / log(num))
        self.primes = np.zeros((num_of_primes,), dtype=BIG)
        self.primes[:3] = [2, 3, 5]
        self.prime_ind = 3
        self.init_primes()
        
        inc_list = np.array([6, 4, 2, 4, 2, 4, 6, 2], dtype=np.uint8)
        inc_index = 0
        
        prime_candidate = 31
        while prime_candidate <= self.n:
            if self.flags[prime_candidate]:
                prime = prime_candidate
                self.found_prime(prime)
            
            prime_candidate += inc_list[inc_index]
            inc_index = (inc_index + 1) % 8
        
        self.primes = self.primes[:self.prime_ind]
        return self.primes

    def init_primes(self):
        initial_primes = np.array([7, 11, 13, 17, 19, 23, 29], dtype=np.uint8)
        for prime in initial_primes:
            self.found_prime(prime)

    def found_prime(self, prime):
        self.primes[self.prime_ind] = prime
        self.prime_ind += 1

        prime_multiple = int(prime) * int(prime)

        if prime_multiple > self.n:
            return
        
        while prime_multiple <= self.n:
            self.flags[prime_multiple] = False
            prime_multiple += prime

class GroupFinder:
    def create_couples(dig):
        ''' Finds couples '''
        # todo: optimize
        primes = Utils.get_req_primes(dig)

        print(f"Calculating couples ...")

        limit = 10**dig

        couples = np.empty((0, 2), dtype=SMALL)

        ind_a = 0
        for ind_a in range(len(primes) - 1):
            a = primes[ind_a]
            if a >= limit:
                break
            for ind_b in range(ind_a + 1, len(primes)):
                b = primes[ind_b]
                if b >= limit:
                    break

                if Utils.check_compatible(primes, a, b):
                    # optimized
                    couples = np.vstack((couples, np.array([a, b], dtype=SMALL)))

        print(f"Couples complete")
        return couples

    def create_triplets(dig):
        ''' given a two-dimensional array that is a list of pairs that
        represents connections, returns a similar list of triplets '''

        couples = Utils.get_couples(dig)

        print(f"Calculating triplets ...")

        couples_len = len(couples)
        triplets = np.empty((0, 3), dtype=SMALL)

        i = 0
        while i < couples_len:
            root = couples[i, 0]

            j = i + 1
            while j < couples_len and couples[j, 0] == root:
                j += 1

            for m in range(i, j - 1):
                for n in range(m + 1, j):
                    a, b = couples[m, 1], couples[n, 1]
                    if Utils.check_couple(couples, [a, b]):
                        new_triplet = np.array([root, a, b], dtype=SMALL)
                        triplets = np.vstack((triplets, new_triplet))

            i = j

        np.savetxt(f'triplets_{dig}dig.txt', triplets, fmt='%d')
        print(f"Triplets complete")
        print(f"Saving as array of type: {triplets.dtype}")
        return triplets

    def create_quadruplets(dig):
        triplets = Utils.get_triplets(dig)

        print(f"Calculating quadruplets ...")

        triplets_len = len(triplets)
        quadruplets = np.empty((0, 4), dtype=SMALL)

        i = 0
        while i < triplets_len:

            a, b = triplets[i][:2]

            j = i + 1
            while j < triplets_len and np.array_equal(triplets[j][:2], [a, b]):
                j += 1

            for m in range(i, j - 1):
                for n in range(m + 1, j):
                    c, d = triplets[m][2], triplets[n][2]
                    if Utils.check_triplet(triplets, [a, c, d]) and Utils.check_triplet(triplets, [b, c, d]):
                        new_quadruplet = np.array([a, b, c, d], dtype=SMALL)
                        quadruplets = np.vstack((quadruplets, new_quadruplet))

            i = j

        print(f"Quadruplets complete")
        return quadruplets

    def create_quintuplets(dig):
        quads = Utils.get_quadruplets(dig)

        print(f"Calculating quintuplets ...")

        quad_len = len(quads)
        quints = np.empty((0, 5), dtype=SMALL)

        i = 0
        while i < quad_len:
            a, b, c = quads[i][:3]

            j = i + 1
            while j < quad_len and np.array_equal(quads[j][:3], [a, b, c]):
                j += 1

            for m in range(i, j - 1):
                for n in range(m + 1, j):
                    d, e = quads[m][3], quads[n][3]
                    if Utils.check_quadruplet(quads, [a, b, d, e]) and \
                            Utils.check_quadruplet(quads, [a, c, d, e]) and \
                            Utils.check_quadruplet(quads, [b, c, d, e]):

                        new_quint = np.array([a, b, c, d, e], dtype=SMALL)
                        quints = np.vstack((quints, new_quint))

            i = j

        print(f"Quintuplets complete")
        return quints

class Utils:
    def get_req_primes(dig):
        prime_value_limit = 10**dig
        prime_count_limit = prime_value_limit**2

        try:
            primes = np.loadtxt(f'primes_until_{prime_count_limit}.txt', dtype=int)
            print(f"Loading primes from primes_until_{prime_count_limit}.txt")
        except IOError:
            print(f"Calculating primes until {prime_count_limit} ...")
            primer = Primer()
            primes = primer.primes_until(prime_count_limit)
            np.savetxt(f'primes_until_{prime_count_limit}.txt', primes, fmt='%d')
            print(f"Primes complete")

        return primes

    def check_compatible(primes, a, b):
        for p in [int(str(a) + str(b)), int(str(b) + str(a))]:
            compatible = False
            left, right = 0, len(primes) - 1
            while left <= right:
                mid = left + (right - left) // 2
                val = primes[mid]
                if p < val:
                    right = mid - 1
                elif p > val:
                    left = mid + 1
                else:
                    compatible = True
                    break
            if not compatible:
                return False
        return True

    def check_couple(arr, couple):
        ''' returns True if couple is in arr, else False '''
        left, right = 0, len(arr) - 1
        a, b = couple
        while left <= right:
            mid = left + (right - left) // 2
            arr_val = arr[mid]
            if a < arr_val[0]:
                right = mid - 1
            elif a > arr_val[0]:
                left = mid + 1
            else:
                if b < arr_val[1]:
                    right = mid - 1
                elif b > arr_val[1]:
                    left = mid + 1
                else:
                    return True
        return False

    def check_triplet(triplets, cand):
        ''' checks if given candidate is in triplets '''
        left, right = 0, len(triplets) - 1
        a, b, c = cand
        while left <= right:
            mid = left + (right - left) // 2
            triplet = triplets[mid]
            if a < triplet[0]:
                right = mid - 1
            elif a > triplet[0]:
                left = mid + 1
            else:
                if b < triplet[1]:
                    right = mid - 1
                elif b > triplet[1]:
                    left = mid + 1
                else:
                    if c < triplet[2]:
                        right = mid - 1
                    elif c > triplet[2]:
                        left = mid + 1
                    else:
                        return True
        return False
    
    def check_quadruplet(quadruplets, cand):
        ''' checks if given candidate is in quadruplets '''
        left, right = 0, len(quadruplets) - 1
        a, b, c, d = cand
        while left <= right:
            mid = left + (right - left) // 2
            quad = quadruplets[mid]
            if a < quad[0]:
                right = mid - 1
            elif a > quad[0]:
                left = mid + 1
            else:
                if b < quad[1]:
                    right = mid - 1
                elif b > quad[1]:
                    left = mid + 1
                else:
                    if c < quad[2]:
                        right = mid - 1
                    elif c > quad[2]:
                        left = mid + 1
                    else:
                        if d < quad[3]:
                            right = mid - 1
                        elif d > quad[3]:
                            left = mid + 1
                        else:
                            return True
        return False


    def get_couples(dig):
        ''' get saved array of specified digit prime couples '''
        try:
            couples = np.loadtxt(f'couples_{dig}dig.txt', dtype=SMALL)
            print(f"Loading couples from couples_{dig}dig.txt")
        except IOError:
            couples = GroupFinder.create_couples(dig)
            np.savetxt(f'couples_{dig}dig.txt', couples, fmt='%d')
            print(f"Saving as array of type: {couples.dtype}")
        return couples

    def get_triplets(dig):
        ''' Returns triplets '''
        try:
            triplets = np.loadtxt(f'triplets_{dig}dig.txt', dtype=SMALL) # int?
            print(f"Loading triplets from triplets_{dig}dig.txt")
        except IOError:
            triplets = GroupFinder.create_triplets(dig)
            np.savetxt(f'triplets_{dig}dig.txt', triplets, fmt='%d')
            print(f"Saving as array of type: {triplets.dtype}")
        return triplets

    def get_quadruplets(dig):
        ''' Calculates quadruplets of specified number of digits
         '''
        try:
            quadruplets = np.loadtxt(f'quadruplets_{dig}dig.txt', dtype=SMALL)
            print(f"Loading quadruplets from quadruplets_{dig}dig.txt")
        except IOError:
            quadruplets = GroupFinder.create_quadruplets(dig)
            np.savetxt(f'quadruplets_{dig}dig.txt', quadruplets, fmt='%d')
            print(f"Saving as array of type: {quadruplets.dtype}")
        return quadruplets

    def get_quintuplets(dig):
        try:
            quintuplets = np.loadtxt(f'quintuplets_{dig}dig.txt', dtype=SMALL)
            print(f"Loading quintuplets from quintuplets_{dig}dig.txt")
        except IOError:
            quintuplets = GroupFinder.create_quintuplets(dig)
            np.savetxt(f'quintuplets_{dig}dig.txt', quintuplets, fmt='%d')
            print(f"Saving as array of type: {quintuplets.dtype}")
        return quintuplets

if __name__ == "__main__":
    quints = Utils.get_quintuplets(4)
    print(quints) # 13 5197 5701 6733 8389

