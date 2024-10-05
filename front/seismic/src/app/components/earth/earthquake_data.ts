type Earthquake = {
    Latitude: number;
    Longitude: number;
    Magnitude: number;
    Date: string;
    Depth: number;
};

export const earthquakeData: Earthquake[] = [
    { Latitude: 51.251, Longitude: 178.715, Magnitude: 8.7, Date: "1965-04-02", Depth: 30.3 },
    { Latitude: 51.443, Longitude: 179.605, Magnitude: 7.3, Date: "1965-04-02", Depth: 30.0 },
    { Latitude: 44.608, Longitude: 149.022, Magnitude: 7.0, Date: "1965-11-06", Depth: 40.7 },
    { Latitude: 44.578, Longitude: 148.699, Magnitude: 7.2, Date: "1965-11-06", Depth: 58.0 },
    { Latitude: 52.99, Longitude: -167.739, Magnitude: 7.8, Date: "1965-02-07", Depth: 45.0 },
    { Latitude: -56.046, Longitude: 157.922, Magnitude: 7.3, Date: "1965-02-08", Depth: 10.0 },
    { Latitude: -15.449, Longitude: 166.98, Magnitude: 7.2, Date: "1965-11-08", Depth: 25.0 },
    { Latitude: -15.861, Longitude: 167.092, Magnitude: 7.6, Date: "1965-11-08", Depth: 30.0 },
    { Latitude: 58.09, Longitude: -152.525, Magnitude: 7.0, Date: "1965-04-09", Depth: 27.8 },
    { Latitude: 24.122, Longitude: 122.583, Magnitude: 7.5, Date: "1966-12-03", Depth: 30.0 },
    { Latitude: 2.388, Longitude: 128.49, Magnitude: 7.7, Date: "1966-08-09", Depth: 115.0 },
    { Latitude: 48.168, Longitude: 103.036, Magnitude: 7.0, Date: "1967-05-01", Depth: 13.2 },
    { Latitude: 2.849, Longitude: -74.798, Magnitude: 7.0, Date: "1967-09-02", Depth: 55.0 },
    { Latitude: -10.656, Longitude: -79.674, Magnitude: 7.0, Date: "1967-03-09", Depth: 15.0 },
    { Latitude: -21.182, Longitude: -179.186, Magnitude: 7.2, Date: "1967-09-10", Depth: 636.8 },
    { Latitude: -5.42, Longitude: 153.368, Magnitude: 7.3, Date: "1968-12-02", Depth: 30.0 },
    { Latitude: 32.449, Longitude: 132.269, Magnitude: 7.5, Date: "1968-01-04", Depth: 34.2 },
    { Latitude: 39.503, Longitude: 143.07, Magnitude: 7.0, Date: "1968-12-06", Depth: 32.1 },
    { Latitude: 16.316, Longitude: 122.067, Magnitude: 7.6, Date: "1968-01-08", Depth: 25.0 },
    { Latitude: 16.519, Longitude: -97.739, Magnitude: 7.3, Date: "1968-02-08", Depth: 25.0 },
    { Latitude: 1.514, Longitude: 126.234, Magnitude: 7.6, Date: "1968-10-08", Depth: 23.0 },
    { Latitude: 26.358, Longitude: 140.635, Magnitude: 7.3, Date: "1968-07-10", Depth: 500.0 },
    { Latitude: -7.97, Longitude: 158.888, Magnitude: 7.0, Date: "1969-05-01", Depth: 60.0 },
    { Latitude: -22.797, Longitude: 178.82, Magnitude: 7.2, Date: "1969-10-02", Depth: 660.0 },
    { Latitude: -6.784, Longitude: 126.581, Magnitude: 7.2, Date: "1969-11-02", Depth: 430.5 },
    { Latitude: 43.599, Longitude: 147.385, Magnitude: 7.5, Date: "1969-11-08", Depth: 25.0 },
    { Latitude: 24.185, Longitude: 102.543, Magnitude: 7.1, Date: "1970-04-01", Depth: 11.3 },
    { Latitude: 6.785, Longitude: 126.682, Magnitude: 7.2, Date: "1970-10-01", Depth: 40.0 },
    { Latitude: 15.791, Longitude: 121.63, Magnitude: 7.4, Date: "1970-07-04", Depth: 25.0 },
    { Latitude: -59.232, Longitude: 158.902, Magnitude: 7.3, Date: "1970-11-06", Depth: 15.0 },
    { Latitude: -11.154, Longitude: 163.377, Magnitude: 7.0, Date: "1970-02-12", Depth: 30.0 },
    { Latitude: -4.026, Longitude: -80.542, Magnitude: 7.2, Date: "1970-10-12", Depth: 25.0 },
    { Latitude: -55.918, Longitude: -2.668, Magnitude: 7.1, Date: "1971-03-01", Depth: 15.0 },
    { Latitude: -3.184, Longitude: 139.722, Magnitude: 7.7, Date: "1971-10-01", Depth: 30.0 },
    { Latitude: 0.653, Longitude: 98.711, Magnitude: 7.0, Date: "1971-04-02", Depth: 30.0 },
    { Latitude: 51.409, Longitude: -176.974, Magnitude: 7.0, Date: "1971-07-02", Depth: 28.9 },
    { Latitude: -63.398, Longitude: -61.377, Magnitude: 7.0, Date: "1971-08-02", Depth: 12.5 },
    { Latitude: -4.33, Longitude: 102.285, Magnitude: 7.0, Date: "1971-08-04", Depth: 75.0 },
    { Latitude: 51.396, Longitude: -177.318, Magnitude: 7.0, Date: "1971-02-05", Depth: 24.2 },
    { Latitude: -32.601, Longitude: -71.076, Magnitude: 7.8, Date: "1971-09-07", Depth: 60.3 },
    { Latitude: 41.415, Longitude: 143.416, Magnitude: 7.1, Date: "1971-02-08", Depth: 54.8 },
    { Latitude: 46.505, Longitude: 141.199, Magnitude: 7.3, Date: "1971-05-09", Depth: 18.1 },
    { Latitude: 3.752, Longitude: 124.221, Magnitude: 7.7, Date: "1972-11-06", Depth: 330.8 },
    { Latitude: -20.122, Longitude: 168.949, Magnitude: 7.0, Date: "1972-02-11", Depth: 20.0 },
    { Latitude: 6.405, Longitude: 126.64, Magnitude: 8.0, Date: "1972-02-12", Depth: 60.0 },
    { Latitude: 33.362, Longitude: 140.827, Magnitude: 7.4, Date: "1972-04-12", Depth: 55.0 },
    { Latitude: 31.398, Longitude: 100.581, Magnitude: 7.4, Date: "1973-06-02", Depth: 33.0 },
    { Latitude: -60.823, Longitude: -21.549, Magnitude: 7.0, Date: "1973-06-10", Depth: 33.0 },
    { Latitude: -14.434, Longitude: 166.863, Magnitude: 7.2, Date: "1974-10-01", Depth: 34.0 },
    { Latitude: -7.383, Longitude: 155.575, Magnitude: 7.1, Date: "1974-01-02", Depth: 40.0 },
    { Latitude: -29.082, Longitude: -175.954, Magnitude: 7.2, Date: "1974-02-07", Depth: 33.0 },
    { Latitude: 39.457, Longitude: 73.83, Magnitude: 7.3, Date: "1974-11-08", Depth: 9.0 },
    { Latitude: -12.265, Longitude: -77.795, Magnitude: 7.6, Date: "1974-03-10", Depth: 13.0 },
    { Latitude: 17.3, Longitude: -62.0, Magnitude: 7.5, Date: "1974-08-10", Depth: 47.0 },
    { Latitude: -12.5, Longitude: -77.786, Magnitude: 7.2, Date: "1974-09-11", Depth: 6.0 },
    { Latitude: 53.113, Longitude: 173.497, Magnitude: 7.6, Date: "1975-02-02", Depth: 10.0 },
    { Latitude: 40.641, Longitude: 122.58, Magnitude: 7.0, Date: "1975-04-02", Depth: 33.0 },
    { Latitude: -38.183, Longitude: -73.232, Magnitude: 7.7, Date: "1975-10-05", Depth: 6.0 },
    { Latitude: 43.024, Longitude: 147.734, Magnitude: 7.0, Date: "1975-10-06", Depth: 15.0 },
    { Latitude: -4.882, Longitude: 102.198, Magnitude: 7.0, Date: "1975-01-10", Depth: 33.0 },
    { Latitude: -12.519, Longitude: 166.499, Magnitude: 7.0, Date: "1975-06-10", Depth: 54.0 },
    { Latitude: -24.894, Longitude: -175.119, Magnitude: 7.8, Date: "1975-11-10", Depth: 9.0 },
    { Latitude: 15.324, Longitude: -89.101, Magnitude: 7.5, Date: "1976-04-02", Depth: 5.0 },
    { Latitude: 40.311, Longitude: 63.773, Magnitude: 7.0, Date: "1976-08-04", Depth: 33.0 },
    { Latitude: 7.409, Longitude: -78.127, Magnitude: 7.0, Date: "1976-11-07", Depth: 3.0 },
    { Latitude: -16.696, Longitude: -172.095, Magnitude: 7.6, Date: "1977-02-04", Depth: 33.0 },
    { Latitude: -25.856, Longitude: -175.406, Magnitude: 7.2, Date: "1977-10-10", Depth: 33.0 },
    { Latitude: -30.683, Longitude: -177.358, Magnitude: 7.2, Date: "1978-09-02", Depth: 33.0 },
    { Latitude: 38.19, Longitude: 142.028, Magnitude: 7.7, Date: "1978-12-06", Depth: 44.0 },
    { Latitude: -11.132, Longitude: 162.136, Magnitude: 7.1, Date: "1978-05-11", Depth: 33.0 },
    { Latitude: -1.679, Longitude: 136.04, Magnitude: 7.9, Date: "1979-12-09", Depth: 5.0 },
    { Latitude: -46.675, Longitude: 165.707, Magnitude: 7.4, Date: "1979-12-10", Depth: 33.0 },
    { Latitude: 1.598, Longitude: -79.358, Magnitude: 7.7, Date: "1979-12-12", Depth: 24.0 },
    { Latitude: -12.41, Longitude: 166.381, Magnitude: 7.5, Date: "1980-08-07", Depth: 33.0 },
    { Latitude: 36.195, Longitude: 1.354, Magnitude: 7.3, Date: "1980-10-10", Depth: 10.0 },
    { Latitude: 41.117, Longitude: -124.253, Magnitude: 7.2, Date: "1980-08-11", Depth: 19.0 },
    { Latitude: -22.293, Longitude: 171.742, Magnitude: 7.0, Date: "1981-06-07", Depth: 33.0 },
    { Latitude: -14.96, Longitude: -173.085, Magnitude: 7.7, Date: "1981-01-09", Depth: 25.0 },
    { Latitude: 13.752, Longitude: 124.358, Magnitude: 7.1, Date: "1982-11-01", Depth: 45.7 },
    { Latitude: 16.558, Longitude: -98.358, Magnitude: 7.0, Date: "1982-07-06", Depth: 33.8 },
    { Latitude: 27.929, Longitude: 136.967, Magnitude: 7.1, Date: "1982-04-07", Depth: 536.0 },
    { Latitude: -51.225, Longitude: 160.513, Magnitude: 7.0, Date: "1982-07-07", Depth: 10.0 },
    { Latitude: -12.597, Longitude: 165.931, Magnitude: 7.0, Date: "1982-05-08", Depth: 30.7 },
    { Latitude: 8.717, Longitude: -83.123, Magnitude: 7.1, Date: "1983-03-04", Depth: 37.0 },
    { Latitude: -4.843, Longitude: -78.103, Magnitude: 7.0, Date: "1983-12-04", Depth: 104.2 },
    { Latitude: -26.535, Longitude: -70.563, Magnitude: 7.4, Date: "1983-04-10", Depth: 14.8 },
    { Latitude: 14.066, Longitude: -91.924, Magnitude: 7.0, Date: "1983-02-12", Depth: 67.1 },
    { Latitude: 33.683, Longitude: 136.894, Magnitude: 7.2, Date: "1984-01-01", Depth: 368.1 },
    { Latitude: -2.823, Longitude: 118.806, Magnitude: 7.0, Date: "1984-08-01", Depth: 33.0 },
    { Latitude: -10.012, Longitude: 160.469, Magnitude: 7.6, Date: "1984-07-02", Depth: 18.1 },
    { Latitude: 8.147, Longitude: 123.762, Magnitude: 7.3, Date: "1984-05-03", Depth: 649.1 },
    { Latitude: 29.384, Longitude: 138.935, Magnitude: 7.4, Date: "1984-06-03", Depth: 457.4 },
    { Latitude: -0.086, Longitude: 122.517, Magnitude: 7.4, Date: "1984-06-08", Depth: 242.3 },
    { Latitude: 8.185, Longitude: -38.794, Magnitude: 7.1, Date: "1984-01-11", Depth: 10.0 },
    { Latitude: -33.135, Longitude: -71.871, Magnitude: 8.0, Date: "1985-03-03", Depth: 33.0 },
    { Latitude: -33.207, Longitude: -71.663, Magnitude: 7.4, Date: "1985-04-03", Depth: 33.0 },
    { Latitude: -34.131, Longitude: -71.618, Magnitude: 7.2, Date: "1985-09-04", Depth: 37.8 },
    { Latitude: -5.599, Longitude: 151.045, Magnitude: 7.2, Date: "1985-10-05", Depth: 26.7 },
    { Latitude: -4.439, Longitude: 152.828, Magnitude: 7.3, Date: "1985-03-07", Depth: 33.0 },
    { Latitude: 51.52, Longitude: -174.776, Magnitude: 8.0, Date: "1986-07-05", Depth: 33.0 },
    { Latitude: -6.088, Longitude: 147.689, Magnitude: 7.4, Date: "1987-08-02", Depth: 54.9 },
    { Latitude: -24.388, Longitude: -70.161, Magnitude: 7.6, Date: "1987-05-03", Depth: 62.3 },
    { Latitude: -24.495, Longitude: -70.701, Magnitude: 7.0, Date: "1987-05-03", Depth: 34.8 },
    { Latitude: 0.151, Longitude: -77.821, Magnitude: 7.2, Date: "1987-06-03", Depth: 10.0 },
    { Latitude: -22.767, Longitude: -66.205, Magnitude: 7.0, Date: "1987-01-04", Depth: 248.7 },
    { Latitude: -19.022, Longitude: -69.991, Magnitude: 7.2, Date: "1987-08-08", Depth: 69.7 },
    { Latitude: -58.893, Longitude: 158.513, Magnitude: 7.4, Date: "1987-03-09", Depth: 33.0 },
    { Latitude: -17.94, Longitude: -172.225, Magnitude: 7.3, Date: "1987-06-10", Depth: 16.0 },
    { Latitude: -7.288, Longitude: 154.371, Magnitude: 7.0, Date: "1987-12-10", Depth: 24.7 },
    { Latitude: -24.753, Longitude: -70.433, Magnitude: 7.2, Date: "1988-05-02", Depth: 36.9 },
    { Latitude: 56.953, Longitude: -143.032, Magnitude: 7.8, Date: "1988-06-03", Depth: 10.0 },
    { Latitude: -17.192, Longitude: -72.305, Magnitude: 7.1, Date: "1988-12-04", Depth: 33.1 },
    { Latitude: 25.149, Longitude: 95.127, Magnitude: 7.3, Date: "1988-06-08", Depth: 90.5 },
    { Latitude: -10.366, Longitude: 160.819, Magnitude: 7.6, Date: "1988-10-08", Depth: 34.0 },
    { Latitude: -18.771, Longitude: -172.415, Magnitude: 7.1, Date: "1988-08-10", Depth: 35.2 },
    { Latitude: 22.789, Longitude: 99.611, Magnitude: 7.7, Date: "1988-06-11", Depth: 17.8 },
    { Latitude: 2.305, Longitude: 126.76, Magnitude: 7.1, Date: "1989-10-02", Depth: 44.0 },
    { Latitude: -8.281, Longitude: -71.381, Magnitude: 7.1, Date: "1989-05-05", Depth: 593.4 },
    { Latitude: 55.543, Longitude: -156.835, Magnitude: 7.1, Date: "1989-04-09", Depth: 11.4 },
    { Latitude: 39.837, Longitude: 142.76, Magnitude: 7.4, Date: "1989-01-11", Depth: 28.6 },
    { Latitude: -6.436, Longitude: 146.383, Magnitude: 7.1, Date: "1989-07-12", Depth: 104.4 },
    { Latitude: -22.122, Longitude: 175.163, Magnitude: 7.6, Date: "1990-03-03", Depth: 33.2 },
    { Latitude: -18.318, Longitude: 168.063, Magnitude: 7.1, Date: "1990-05-03", Depth: 20.7 },
    { Latitude: 15.125, Longitude: 147.596, Magnitude: 7.6, Date: "1990-05-04", Depth: 11.4 },
    { Latitude: 49.037, Longitude: 141.847, Magnitude: 7.2, Date: "1990-12-05", Depth: 605.7 },
    { Latitude: -19.435, Longitude: 169.132, Magnitude: 7.1, Date: "1990-12-08", Depth: 140.4 },
    { Latitude: 53.452, Longitude: 169.871, Magnitude: 7.1, Date: "1990-06-11", Depth: 24.8 },
    { Latitude: 23.613, Longitude: 95.901, Magnitude: 7.0, Date: "1991-05-01", Depth: 19.7 },
    { Latitude: -5.982, Longitude: -77.094, Magnitude: 7.1, Date: "1991-05-04", Depth: 19.8 },
    { Latitude: -20.252, Longitude: -176.218, Magnitude: 7.0, Date: "1991-09-06", Depth: 265.5 },
    { Latitude: -13.108, Longitude: -72.187, Magnitude: 7.0, Date: "1991-06-07", Depth: 104.5 },
    { Latitude: -22.483, Longitude: -178.413, Magnitude: 7.2, Date: "1992-11-07", Depth: 377.2 },
    { Latitude: 11.742, Longitude: -87.34, Magnitude: 7.7, Date: "1992-02-09", Depth: 44.8 },
    { Latitude: -19.247, Longitude: 168.948, Magnitude: 7.4, Date: "1992-11-10", Depth: 129.0 },
    { Latitude: -8.48, Longitude: 121.896, Magnitude: 7.8, Date: "1992-12-12", Depth: 27.7 },
    { Latitude: -10.972, Longitude: 164.181, Magnitude: 7.1, Date: "1993-06-03", Depth: 20.4 },
    { Latitude: 7.219, Longitude: 126.57, Magnitude: 7.0, Date: "1993-11-05", Depth: 58.7 },
    { Latitude: 51.218, Longitude: 157.829, Magnitude: 7.5, Date: "1993-08-06", Depth: 70.6 },
    { Latitude: 42.851, Longitude: 139.197, Magnitude: 7.7, Date: "1993-12-07", Depth: 16.7 },
    { Latitude: 12.982, Longitude: 144.801, Magnitude: 7.8, Date: "1993-08-08", Depth: 59.3 },
    { Latitude: 36.379, Longitude: 70.868, Magnitude: 7.0, Date: "1993-09-08", Depth: 214.5 },
    { Latitude: -45.277, Longitude: 166.927, Magnitude: 7.0, Date: "1993-10-08", Depth: 28.1 },
    { Latitude: 14.717, Longitude: -92.645, Magnitude: 7.2, Date: "1993-10-09", Depth: 34.1 },
    { Latitude: -20.553, Longitude: 169.361, Magnitude: 7.0, Date: "1994-12-02", Depth: 27.7 },
    { Latitude: -18.039, Longitude: -178.413, Magnitude: 7.6, Date: "1994-09-03", Depth: 562.5 },
    { Latitude: -10.477, Longitude: 112.835, Magnitude: 7.8, Date: "1994-02-06", Depth: 18.4 },
    { Latitude: -13.841, Longitude: -67.553, Magnitude: 8.2, Date: "1994-09-06", Depth: 631.3 },
    { Latitude: 40.4055, Longitude: -126.3028333, Magnitude: 7.0, Date: "1994-01-09", Depth: 4.972 },
    { Latitude: 43.773, Longitude: 147.321, Magnitude: 8.3, Date: "1994-04-10", Depth: 14.0 },
    { Latitude: 43.905, Longitude: 147.916, Magnitude: 7.3, Date: "1994-09-10", Depth: 33.0 },
    { Latitude: 40.246, Longitude: 142.175, Magnitude: 7.0, Date: "1995-06-01", Depth: 26.9 },
    { Latitude: -37.759, Longitude: 178.752, Magnitude: 7.1, Date: "1995-05-02", Depth: 21.1 },
    { Latitude: -15.199, Longitude: -173.529, Magnitude: 7.4, Date: "1995-07-04", Depth: 21.2 },
    { Latitude: 12.626, Longitude: 125.297, Magnitude: 7.1, Date: "1995-05-05", Depth: 16.0 },
    { Latitude: -29.211, Longitude: -177.589, Magnitude: 7.2, Date: "1995-03-07", Depth: 35.3 },
    { Latitude: -2.75, Longitude: -77.881, Magnitude: 7.0, Date: "1995-03-10", Depth: 24.4 },
    { Latitude: 19.055, Longitude: -104.205, Magnitude: 8.0, Date: "1995-09-10", Depth: 33.0 },
    { Latitude: 44.663, Longitude: 149.3, Magnitude: 7.9, Date: "1995-03-12", Depth: 33.0 },
    { Latitude: 0.729, Longitude: 119.931, Magnitude: 7.9, Date: "1996-01-01", Depth: 24.0 },
    { Latitude: 45.324, Longitude: 149.892, Magnitude: 7.2, Date: "1996-07-02", Depth: 42.6 },
    { Latitude: 10.797, Longitude: -42.254, Magnitude: 7.0, Date: "1996-02-06", Depth: 10.0 },
    { Latitude: 51.564, Longitude: -177.632, Magnitude: 7.9, Date: "1996-10-06", Depth: 33.0 },
    { Latitude: 51.478, Longitude: -176.847, Magnitude: 7.3, Date: "1996-10-06", Depth: 26.3 },
    { Latitude: 12.614, Longitude: 125.154, Magnitude: 7.1, Date: "1996-11-06", Depth: 33.0 },
    { Latitude: -20.69, Longitude: -178.31, Magnitude: 7.4, Date: "1996-05-08", Depth: 550.2 },
    { Latitude: -14.993, Longitude: -75.675, Magnitude: 7.7, Date: "1996-12-11", Depth: 33.0 },
    { Latitude: 18.219, Longitude: -102.756, Magnitude: 7.2, Date: "1997-11-01", Depth: 33.0 },
    { Latitude: 33.825, Longitude: 59.809, Magnitude: 7.3, Date: "1997-10-05", Depth: 10.0 },
    { Latitude: 10.598, Longitude: -63.486, Magnitude: 7.0, Date: "1997-09-07", Depth: 19.9 },
    { Latitude: 35.069, Longitude: 87.325, Magnitude: 7.5, Date: "1997-08-11", Depth: 33.0 },
    { Latitude: 54.841, Longitude: 162.035, Magnitude: 7.8, Date: "1997-05-12", Depth: 33.0 },
    { Latitude: -22.301, Longitude: 170.911, Magnitude: 7.5, Date: "1998-04-01", Depth: 100.6 },
    { Latitude: -0.544, Longitude: 99.261, Magnitude: 7.0, Date: "1998-01-04", Depth: 55.7 },
    { Latitude: 22.306, Longitude: 125.308, Magnitude: 7.5, Date: "1998-03-05", Depth: 33.0 },
    { Latitude: -0.593, Longitude: -80.393, Magnitude: 7.2, Date: "1998-04-08", Depth: 33.0 },
    { Latitude: -6.92, Longitude: 128.946, Magnitude: 7.0, Date: "1998-09-11", Depth: 33.0 },
    { Latitude: -12.853, Longitude: 166.697, Magnitude: 7.3, Date: "1999-06-02", Depth: 90.1 },
    { Latitude: 5.397, Longitude: 121.937, Magnitude: 7.1, Date: "1999-04-03", Depth: 33.0 },
    { Latitude: -5.591, Longitude: 149.568, Magnitude: 7.4, Date: "1999-05-04", Depth: 150.0 },
    { Latitude: 43.607, Longitude: 130.35, Magnitude: 7.1, Date: "1999-08-04", Depth: 565.7 },
    { Latitude: -5.159, Longitude: 150.88, Magnitude: 7.1, Date: "1999-10-05", Depth: 138.0 },
    { Latitude: 40.758, Longitude: 31.161, Magnitude: 7.2, Date: "1999-12-11", Depth: 10.0 },
    { Latitude: 57.413, Longitude: -154.489, Magnitude: 7.0, Date: "1999-06-12", Depth: 66.0 },
    { Latitude: 15.766, Longitude: 119.74, Magnitude: 7.3, Date: "1999-11-12", Depth: 33.0 },
    { Latitude: -16.925, Longitude: -174.248, Magnitude: 7.2, Date: "2000-08-01", Depth: 183.4 },
    { Latitude: -1.105, Longitude: 123.573, Magnitude: 7.6, Date: "2000-04-05", Depth: 26.0 },
    { Latitude: -23.548, Longitude: -66.452, Magnitude: 7.2, Date: "2000-12-05", Depth: 225.0 },
    { Latitude: -4.721, Longitude: 102.087, Magnitude: 7.9, Date: "2000-04-06", Depth: 33.0 },
    { Latitude: 28.856, Longitude: 139.556, Magnitude: 7.4, Date: "2000-06-08", Depth: 394.8 },
    { Latitude: -15.421, Longitude: 166.91, Magnitude: 7.0, Date: "2000-04-10", Depth: 23.0 },
    { Latitude: 39.566, Longitude: 54.799, Magnitude: 7.0, Date: "2000-06-12", Depth: 30.0 },
    { Latitude: 6.898, Longitude: 126.579, Magnitude: 7.5, Date: "2001-01-01", Depth: 33.0 },
    { Latitude: -14.928, Longitude: 167.17, Magnitude: 7.1, Date: "2001-09-01", Depth: 103.0 },
    { Latitude: 57.078, Longitude: -153.211, Magnitude: 7.0, Date: "2001-10-01", Depth: 33.0 },
    { Latitude: -29.666, Longitude: -178.633, Magnitude: 7.2, Date: "2001-03-06", Depth: 178.1 },
    { Latitude: -17.543, Longitude: -72.077, Magnitude: 7.6, Date: "2001-07-07", Depth: 33.0 },
    { Latitude: 12.686, Longitude: 144.98, Magnitude: 7.0, Date: "2001-12-10", Depth: 37.0 },
    { Latitude: -42.813, Longitude: 124.688, Magnitude: 7.1, Date: "2001-12-12", Depth: 10.0 },
    { Latitude: -17.6, Longitude: 167.856, Magnitude: 7.2, Date: "2002-02-01", Depth: 21.0 },
    { Latitude: 36.502, Longitude: 70.482, Magnitude: 7.4, Date: "2002-03-03", Depth: 225.6 },
    { Latitude: 6.033, Longitude: 124.249, Magnitude: 7.5, Date: "2002-05-03", Depth: 31.0 },
    { Latitude: -3.302, Longitude: 142.945, Magnitude: 7.6, Date: "2002-08-09", Depth: 13.0 },
    { Latitude: -1.757, Longitude: 134.297, Magnitude: 7.6, Date: "2002-10-10", Depth: 10.0 },
    { Latitude: 2.824, Longitude: 96.085, Magnitude: 7.4, Date: "2002-02-11", Depth: 30.0 },
    { Latitude: 63.517, Longitude: -147.444, Magnitude: 7.9, Date: "2002-03-11", Depth: 4.9 },
    { Latitude: -60.532, Longitude: -43.411, Magnitude: 7.6, Date: "2003-04-08", Depth: 10.0 },
    { Latitude: -22.253, Longitude: 169.683, Magnitude: 7.1, Date: "2004-03-01", Depth: 22.0 },
    { Latitude: -3.615, Longitude: 135.538, Magnitude: 7.0, Date: "2004-05-02", Depth: 16.6 },
    { Latitude: -4.003, Longitude: 135.023, Magnitude: 7.3, Date: "2004-07-02", Depth: 10.0 },
    { Latitude: 33.07, Longitude: 136.618, Magnitude: 7.2, Date: "2004-05-09", Depth: 14.0 },
    { Latitude: 33.184, Longitude: 137.071, Magnitude: 7.4, Date: "2004-05-09", Depth: 10.0 },
    { Latitude: 11.422, Longitude: -86.665, Magnitude: 7.0, Date: "2004-09-10", Depth: 35.0 },
    { Latitude: -8.152, Longitude: 124.868, Magnitude: 7.5, Date: "2004-11-11", Depth: 10.0 },
    { Latitude: 5.293, Longitude: 123.337, Magnitude: 7.1, Date: "2005-05-02", Depth: 525.0 },
    { Latitude: -6.527, Longitude: 129.933, Magnitude: 7.1, Date: "2005-02-03", Depth: 201.7 },
    { Latitude: -4.539, Longitude: 153.474, Magnitude: 7.6, Date: "2005-09-09", Depth: 90.0 },
    { Latitude: 34.539, Longitude: 73.588, Magnitude: 7.6, Date: "2005-08-10", Depth: 26.0 },
    { Latitude: -60.957, Longitude: -21.606, Magnitude: 7.4, Date: "2006-02-01", Depth: 13.0 },
    { Latitude: -19.926, Longitude: -178.178, Magnitude: 7.2, Date: "2006-02-01", Depth: 582.9 },
    { Latitude: -20.187, Longitude: -174.123, Magnitude: 8.0, Date: "2006-03-05", Depth: 55.0 },
    { Latitude: -8.466, Longitude: 157.043, Magnitude: 8.1, Date: "2007-01-04", Depth: 24.0 },
    { Latitude: -15.595, Longitude: 167.68, Magnitude: 7.2, Date: "2007-01-08", Depth: 120.0 },
    { Latitude: -5.859, Longitude: 107.419, Magnitude: 7.5, Date: "2007-08-08", Depth: 280.0 },
    { Latitude: -11.61, Longitude: 165.762, Magnitude: 7.2, Date: "2007-02-09", Depth: 35.0 },
    { Latitude: -4.438, Longitude: 101.367, Magnitude: 8.4, Date: "2007-12-09", Depth: 34.0 },
    { Latitude: -2.625, Longitude: 100.841, Magnitude: 7.9, Date: "2007-12-09", Depth: 35.0 },
    { Latitude: -25.996, Longitude: -177.514, Magnitude: 7.8, Date: "2007-09-12", Depth: 152.5 },
    { Latitude: -20.071, Longitude: 168.892, Magnitude: 7.3, Date: "2008-09-04", Depth: 33.0 },
    { Latitude: -55.664, Longitude: 158.453, Magnitude: 7.1, Date: "2008-12-04", Depth: 16.0 },
    { Latitude: 31.002, Longitude: 103.322, Magnitude: 7.9, Date: "2008-12-05", Depth: 19.0 },
    { Latitude: 53.882, Longitude: 152.886, Magnitude: 7.7, Date: "2008-05-07", Depth: 632.8 },
    { Latitude: -0.414, Longitude: 132.885, Magnitude: 7.7, Date: "2009-03-01", Depth: 17.0 },
    { Latitude: -0.691, Longitude: 133.305, Magnitude: 7.4, Date: "2009-03-01", Depth: 23.0 },
    { Latitude: 3.886, Longitude: 126.387, Magnitude: 7.2, Date: "2009-11-02", Depth: 20.0 },
    { Latitude: 33.167, Longitude: 137.944, Magnitude: 7.1, Date: "2009-09-08", Depth: 292.0 },
    { Latitude: 14.099, Longitude: 92.902, Magnitude: 7.5, Date: "2009-10-08", Depth: 24.0 },
    { Latitude: -7.782, Longitude: 107.297, Magnitude: 7.0, Date: "2009-02-09", Depth: 46.0 },
    { Latitude: -13.006, Longitude: 166.51, Magnitude: 7.7, Date: "2009-07-10", Depth: 45.0 },
    { Latitude: -12.517, Longitude: 166.382, Magnitude: 7.8, Date: "2009-07-10", Depth: 35.0 },
    { Latitude: -13.093, Longitude: 166.497, Magnitude: 7.4, Date: "2009-07-10", Depth: 31.1 },
    { Latitude: -17.239, Longitude: 178.331, Magnitude: 7.3, Date: "2009-09-11", Depth: 595.0 },
    { Latitude: -8.783, Longitude: 157.354, Magnitude: 7.1, Date: "2010-03-01", Depth: 10.0 },
    { Latitude: 18.443, Longitude: -72.571, Magnitude: 7.0, Date: "2010-12-01", Depth: 13.0 },
    { Latitude: -34.326, Longitude: -71.799, Magnitude: 7.0, Date: "2010-11-03", Depth: 18.0 },
    { Latitude: 32.2861667, Longitude: -115.2953333, Magnitude: 7.2, Date: "2010-04-04", Depth: 9.987 },
    { Latitude: 2.383, Longitude: 97.048, Magnitude: 7.8, Date: "2010-06-04", Depth: 31.0 },
    { Latitude: 3.748, Longitude: 96.018, Magnitude: 7.2, Date: "2010-09-05", Depth: 38.0 },
    { Latitude: 7.881, Longitude: 91.936, Magnitude: 7.5, Date: "2010-12-06", Depth: 35.0 },
    { Latitude: -5.746, Longitude: 150.765, Magnitude: 7.0, Date: "2010-04-08", Depth: 44.0 },
    { Latitude: -17.541, Longitude: 168.069, Magnitude: 7.3, Date: "2010-10-08", Depth: 25.0 },
    { Latitude: -1.266, Longitude: -77.306, Magnitude: 7.1, Date: "2010-12-08", Depth: 206.7 },
    { Latitude: -43.522, Longitude: 171.83, Magnitude: 7.0, Date: "2010-03-09", Depth: 12.0 },
    { Latitude: -26.803, Longitude: -63.136, Magnitude: 7.0, Date: "2011-01-01", Depth: 576.8 },
    { Latitude: -38.355, Longitude: -73.326, Magnitude: 7.2, Date: "2011-02-01", Depth: 24.0 },
    { Latitude: 38.435, Longitude: 142.842, Magnitude: 7.3, Date: "2011-09-03", Depth: 32.0 },
    { Latitude: 38.297, Longitude: 142.373, Magnitude: 9.1, Date: "2011-11-03", Depth: 29.0 },
    { Latitude: 36.281, Longitude: 141.111, Magnitude: 7.9, Date: "2011-11-03", Depth: 42.6 },
    { Latitude: 38.058, Longitude: 144.59, Magnitude: 7.7, Date: "2011-11-03", Depth: 18.6 },
    { Latitude: 38.276, Longitude: 141.588, Magnitude: 7.1, Date: "2011-07-04", Depth: 42.0 },
    { Latitude: -29.539, Longitude: -176.34, Magnitude: 7.6, Date: "2011-06-07", Depth: 17.0 },
    { Latitude: 38.034, Longitude: 143.264, Magnitude: 7.0, Date: "2011-10-07", Depth: 23.0 },
    { Latitude: -20.671, Longitude: 169.716, Magnitude: 7.0, Date: "2011-03-09", Depth: 185.1 },
    { Latitude: 2.433, Longitude: 93.21, Magnitude: 7.2, Date: "2012-10-01", Depth: 19.0 },
    { Latitude: -17.827, Longitude: 167.133, Magnitude: 7.1, Date: "2012-02-02", Depth: 23.0 },
    { Latitude: 2.327, Longitude: 93.063, Magnitude: 8.6, Date: "2012-11-04", Depth: 20.0 },
    { Latitude: 0.802, Longitude: 92.463, Magnitude: 8.2, Date: "2012-11-04", Depth: 25.1 },
    { Latitude: 28.696, Longitude: -113.104, Magnitude: 7.0, Date: "2012-12-04", Depth: 13.0 },
    { Latitude: 10.085, Longitude: -85.315, Magnitude: 7.6, Date: "2012-05-09", Depth: 35.0 },
    { Latitude: 13.988, Longitude: -91.895, Magnitude: 7.4, Date: "2012-07-11", Depth: 24.0 },
    { Latitude: 37.89, Longitude: 143.949, Magnitude: 7.3, Date: "2012-07-12", Depth: 31.0 },
    { Latitude: -6.533, Longitude: 129.825, Magnitude: 7.1, Date: "2012-10-12", Depth: 155.0 },
    { Latitude: 55.393, Longitude: -134.652, Magnitude: 7.5, Date: "2013-05-01", Depth: 10.0 },
    { Latitude: -10.799, Longitude: 165.114, Magnitude: 8.0, Date: "2013-06-02", Depth: 24.0 },
    { Latitude: -11.183, Longitude: 164.882, Magnitude: 7.1, Date: "2013-06-02", Depth: 10.0 },
    { Latitude: -10.499, Longitude: 165.588, Magnitude: 7.0, Date: "2013-06-02", Depth: 8.8 },
    { Latitude: -10.928, Longitude: 166.018, Magnitude: 7.1, Date: "2013-08-02", Depth: 21.0 },
    { Latitude: -3.517, Longitude: 138.476, Magnitude: 7.0, Date: "2013-06-04", Depth: 66.0 },
    { Latitude: -3.917, Longitude: 153.927, Magnitude: 7.3, Date: "2013-07-07", Depth: 385.5 },
    { Latitude: -19.6097, Longitude: -70.7691, Magnitude: 8.2, Date: "2014-01-04", Depth: 25.0 },
    { Latitude: -20.5709, Longitude: -70.4931, Magnitude: 7.7, Date: "2014-03-04", Depth: 22.4 },
    { Latitude: -6.5858, Longitude: 155.0485, Magnitude: 7.1, Date: "2014-11-04", Depth: 60.53 },
    { Latitude: -11.2701, Longitude: 162.1481, Magnitude: 7.6, Date: "2014-12-04", Depth: 22.56 },
    { Latitude: -32.1082, Longitude: -110.8112, Magnitude: 7.0, Date: "2014-09-10", Depth: 16.54 },
    { Latitude: -19.6903, Longitude: -177.7587, Magnitude: 7.1, Date: "2014-01-11", Depth: 434.0 },
    { Latitude: -5.4624, Longitude: 151.8751, Magnitude: 7.5, Date: "2015-05-05", Depth: 55.0 },
    { Latitude: -7.2175, Longitude: 154.5567, Magnitude: 7.1, Date: "2015-07-05", Depth: 10.0 },
    { Latitude: 27.8087, Longitude: 86.0655, Magnitude: 7.3, Date: "2015-12-05", Depth: 15.0 },
    { Latitude: -47.6165, Longitude: 85.0913, Magnitude: 7.1, Date: "2015-04-12", Depth: 35.0 },
    { Latitude: 38.2107, Longitude: 72.7797, Magnitude: 7.2, Date: "2015-07-12", Depth: 22.0 },
    { Latitude: -4.9521, Longitude: 94.3299, Magnitude: 7.8, Date: "2016-02-03", Depth: 24.0 },
    { Latitude: -22.4765, Longitude: 173.1167, Magnitude: 7.2, Date: "2016-12-08", Depth: 16.37 },
    { Latitude: -37.3586, Longitude: 179.1461, Magnitude: 7.0, Date: "2016-01-09", Depth: 19.0 },
    { Latitude: -10.6787, Longitude: 161.3214, Magnitude: 7.8, Date: "2016-08-12", Depth: 40.0 }
];