import sa
import argparse

usa =      [sa.City(6734, 1453),
            sa.City(2233,  10),
            sa.City(5530, 1424),
             sa.City(401,  841),
            sa.City(3082, 1644),
            sa.City(7608, 4458),
            sa.City(7573, 3716),
            sa.City(7265, 1268),
            sa.City(6898, 1885),
            sa.City(1112, 2049),
            sa.City(5468, 2606),
            sa.City(5989, 2873),
            sa.City(4706, 2674),
            sa.City(4612, 2035),
            sa.City(6347, 2683),
            sa.City(6107,  669),
            sa.City(7611, 5184),
            sa.City(7462, 3590),
            sa.City(7732, 4723),
            sa.City(5900, 3561),
            sa.City(4483, 3369),
            sa.City(6101, 1110),
            sa.City(5199, 2182),
            sa.City(1633, 2809),
            sa.City(4307, 2322),
            sa.City( 675, 1006),
            sa.City(7555, 4819),
            sa.City(7541, 3981),
            sa.City(3177,  756),
            sa.City(7352, 4506),
            sa.City(7545, 2801),
            sa.City(3245, 3305),
            sa.City(6426, 3173),
            sa.City(4608, 1198),
              sa.City(23, 2216),
            sa.City(7248, 3779),
            sa.City(7762, 4595),
            sa.City(7392, 2244),
            sa.City(3484, 2829),
            sa.City(6271, 2135),
            sa.City(4985,  140),
            sa.City(1916, 1569),
            sa.City(7280, 4899),
            sa.City(7509, 3239),
              sa.City(10, 2676),
            sa.City(6807, 2993),
            sa.City(5185, 3258),
            sa.City(3023, 1942)]

##########################################################################
# Main
if __name__ == "__main__":

    # arg parser
    description = 'TSP solver using simulated annealing'
    p = argparse.ArgumentParser(description = description)
    p.add_argument("max_iterations", help="Maximum number of iterations used by SA")
    p.add_argument("mode", help="Solving method: standard, ex0, ex1")
    args = p.parse_args()

    # convert args
    max_iterations = int(args.max_iterations)

    # create cities
    cities = usa

    max_coord = 0;
    for city in cities:
        if(city.x > max_coord):
            max_coord = city.x
        if(city.y > max_coord):
            max_coord = city.y

    for city in cities:
        city.x /= max_coord
        city.y /= max_coord

    # run the solver
    solver = sa.Solver(cities,max_iterations)
    solver.animate(args.mode)



