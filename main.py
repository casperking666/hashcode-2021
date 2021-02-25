import analyze
import read_file
import collector
import output


def process(name):
    a,b,c=read_file.readfile(name)
    output.writeFile(analyze.getInput(collector.data_collection(a,b,c)))




if __name__ == '__main__':
    process("b.txt")