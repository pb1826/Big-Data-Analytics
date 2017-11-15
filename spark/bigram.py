from __future__ import print_function

import sys
from operator import add
from pyspark import SparkContext


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: bigram <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    sentences = lines.glom() \
                  .map(lambda x: " ".join(x)) \
                  .flatMap(lambda x: x.split("."))

    #Your code goes here
    bigrams = sentences.map(lambda a:a.split()).flatMap(lambda a: [((a[i],a[i+1]),1) for i in range(0,len(a)-1)])
    result = bigrams.reduceByKey( lambda a,b:a+b)\
                    .map(lambda a: (a[1],a[0])).sortByKey(False).take(100)
    
    output = sc.parallelize(result)
    output.saveAsTextFile("frequency.out")
    

    sc.stop()
