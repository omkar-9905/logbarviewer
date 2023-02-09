
import matplotlib.pyplot as plt

def info(data):
    info = []
    for i in data:
        if "INFO" in i:
            info.append(i)
    return len(info)

def warning(data):
    warn = []
    for i in data:
        if "WARNING" in i:
            warn.append(i)
    return len(warn)

def error(data):
    error = []
    for i in data:
        if "ERROR" in i:
            error.append(i)
    return len(error)

def show_chart(val1,val2,val3):
    country = ['info','warn','error']
    gdp_per_capita = [val1,val2,val3]

    plt.bar(country, gdp_per_capita)
    plt.title('info vs warn vs error')
    plt.xlabel('Log Levels')
    plt.ylabel('Number Of Logs')
    plt.show()

if __name__=='__main__':
    data = []
    with open("logfileviewer/sample.log",'r') as f:
        for i in f:
            data.append(i)
    show_chart(info(data),warning(data),error(data))
