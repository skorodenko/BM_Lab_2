

def plot_points(in_file, out_file, interactive=False) -> None:
    """ This function plots data from file
    :param in_file: text file with x,y coordiante of points
    :param out_file: file to save plot
    :param interactive: bool, if True show interective pyplot GUI, if False save to file

    in_file should contain data in next format:
    2 3
    4 5
    3 5
    ...
    """
    # Loading data from dataset
    data = numpy.loadtxt(DataSet)

    # Splitting data, into two sub arrays
    # X - cooridnates on X axis
    # Y - coordinates in Y axis
    X, Y = numpy.hsplit(data, 2)
    # Plotting data
    plt.plot(Y, X, "o")
    # Setting canvas size to 540x960
    plt.axis([0, 960, 0, 540])
    
    # Show Pyplot GUI or not
    if interactive:
        plt.show()
    else:
        plt.savefig(out_file)


if __name__ == "__main__":
    import numpy
    import matplotlib.pyplot as plt

    DataSet = "DS8.txt"
    OutFile = "DS8.png"
    plot_points(DataSet, OutFile)
