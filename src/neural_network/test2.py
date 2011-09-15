from network import NeuralNetwork

data = [
    {
        'input': [
            4,4,4,4,4,
            4,0,0,0,4,
            4,0,0,0,4,
            4,0,0,0,4,
            4,0,0,0,4,
            4,0,0,0,4,
            4,4,4,4,4
        ],
        'output': [1, 0, 0, 0, 0]
    },
    {
        'input': [
            0,0,0,0,4,
            0,0,0,0,4,
            0,0,0,0,4,
            0,0,0,0,4,
            0,0,0,0,4,
            0,0,0,0,4,
            0,0,0,0,4
        ],
        'output': [0, 1, 0, 0, 0]
    },        
    {
        'input': [
            0,0,4,4,4,
            0,0,0,0,4,
            0,0,0,4,0,
            0,0,4,0,0,
            0,4,0,0,0,
            4,0,0,0,0,
            4,4,4,4,4
        ],
        'output': [0, 0, 1, 0, 0]
    },        
    {
        'input': [
            0,4,4,4,0,
            4,0,0,0,4,
            0,0,0,0,4,
            0,0,0,4,0,
            0,0,0,0,4,
            4,0,0,0,4,
            0,4,4,4,0
        ],
        'output': [0, 0, 0, 1, 0]
    },
    {
        'input': [
            4,4,4,4,4,
            4,0,0,0,0,
            4,0,0,0,0,
            4,4,4,4,0,
            0,0,0,0,4,
            0,0,0,0,4,
            4,4,4,4,0
        ],
        'output': [0, 0, 0, 0, 1]
    }                    
]

test_data = [
    {
        'input': [
            4,4,4,4,4,
            4,1,1,1,4,
            4,1,1,1,4,
            4,1,1,1,4,
            4,1,1,1,4,
            4,1,1,1,4,
            4,4,4,4,4
        ],
        'output': [1, 0, 0, 0, 0]
    },
    {
        'input': [
            0,0,0,0,4,
            0,0,0,4,4,
            0,0,4,0,4,
            0,0,0,0,4,
            0,0,0,0,4,
            0,0,0,0,4,
            0,0,0,0,4
        ],
        'output': [0, 1, 0, 0, 0]
    },        
    {
        'input': [
            1,0,4,4,4,
            1,0,0,0,4,
            0,0,0,4,0,
            0,0,4,0,0,
            0,4,0,0,0,
            4,0,0,0,4,
            4,4,4,4,4
        ],
        'output': [0, 0, 1, 0, 0]
    },
    {
        'input': [
            4,4,4,4,0,
            0,0,0,0,4,
            0,0,0,0,4,
            0,0,0,4,0,
            0,0,0,0,4,
            0,0,0,0,4,
            4,4,4,4,0
        ],
        'output': [0, 0, 0, 1, 0]
    },
    {
        'input': [
            4,4,4,4,4,
            4,0,0,0,0,
            4,1,1,1,0,
            4,4,4,4,4,
            0,4,0,1,4,
            0,0,2,0,4,
            4,4,4,4,0
        ],
        'output': [0, 0, 0, 0, 1]
    }                                                       
]

#Example of output
#Check study
#['0.96', '0.02', '0.01', '0.02', '0.03'] ['1.00', '0.00', '0.00', '0.00', '0.00']
#['0.02', '0.97', '0.02', '0.02', '0.01'] ['0.00', '1.00', '0.00', '0.00', '0.00']
#['0.02', '0.01', '0.96', '0.02', '0.02'] ['0.00', '0.00', '1.00', '0.00', '0.00']
#['0.02', '0.02', '0.02', '0.96', '0.02'] ['0.00', '0.00', '0.00', '1.00', '0.00']
#['0.03', '0.01', '0.03', '0.02', '0.96'] ['0.00', '0.00', '0.00', '0.00', '1.00']
#Check study
#['0.94', '0.02', '0.01', '0.01', '0.04'] ['1.00', '0.00', '0.00', '0.00', '0.00']
#['0.03', '0.95', '0.02', '0.01', '0.01'] ['0.00', '1.00', '0.00', '0.00', '0.00']
#['0.02', '0.02', '0.95', '0.02', '0.02'] ['0.00', '0.00', '1.00', '0.00', '0.00']
#['0.03', '0.01', '0.05', '0.87', '0.02'] ['0.00', '0.00', '0.00', '1.00', '0.00']
#['0.03', '0.01', '0.05', '0.02', '0.95'] ['0.00', '0.00', '0.00', '0.00', '1.00']


if __name__ == "__main__":
    network = NeuralNetwork((5*7, 5*7/2, 5))
    network.teach(data, max_retries=1000)
    print 'Check study'
    network.test(data)
    print 'Check study'
    network.test(test_data)    