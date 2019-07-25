def _read_s_parameters():
        """Returns the s-parameters across some frequency range for the ebeam_dc_halfring_te1550 model
        in the form [frequency, s-parameters].

        Parameters
        ----------
        numports : int
            The number of ports the photonic component has.
        """
        numports = 4
        filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), "sparams", "ebeam_dc_halfring_te1550", "te_ebeam_dc_halfring_straight_gap=30nm_radius=3um_width=520nm_thickness=210nm_CoupleLength=0um.dat")
        F = []
        S = []
        with open(filename, "r") as fid:
            for i in range(5):
                line = fid.readline()
            line = fid.readline()
            numrows = int(tuple(line[1:-2].split(','))[0])
            S = np.zeros((numrows, numports, numports), dtype='complex128')
            r = m = n = 0
            for line in fid:
                if(line[0] == '('):
                    continue
                data = line.split()
                data = list(map(float, data))
                if(m == 0 and n == 0):
                    F.append(data[0])
                S[r,m,n] = data[1] * np.exp(1j*data[2])
                r += 1
                if(r == numrows):
                    r = 0
                    m += 1
                    if(m == numports):
                        m = 0
                        n += 1
                        if(n == numports):
                            break
        return (F, S)
