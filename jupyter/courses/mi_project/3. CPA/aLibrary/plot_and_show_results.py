import matplotlib.pyplot as plt
import IPython.display as _display
import numpy as np
import math
import scared

figure_axes_text_size = 14
graph_title_fontsize = 14

RED_TEXT = '\033[31m'
GREEN_TEXT = '\033[32m'

color_all_guesses = 'grey'
color_best_guess = 'green'
color_right_guess = 'dodgerblue'

 
def plot_attack_result_single_byte(attack_object, key_byte=0, correct_key=None):
    DOWNS_STEP = 1
    guesses_number = attack_object.results.shape[0]
    best_guesses = attack_object.scores.argmax(0).squeeze()

    if attack_object.convergence_step is not None:
        CONV_POINTS =  attack_object.convergence_traces.shape[2]
        # Plot result traces
        plt.subplot(1,2,1)
        for i in range(guesses_number): plt.plot(attack_object.results[i,key_byte].T[:-1:DOWNS_STEP], color = color_all_guesses)
        plt.plot(attack_object.results[best_guesses[key_byte],key_byte].T[:-1:DOWNS_STEP], color = color_best_guess, label='best score')
        if correct_key is not None: 
            plt.plot(attack_object.results[correct_key[key_byte],key_byte].T[:-1:DOWNS_STEP], color = color_right_guess, label='right key')
        # Set axes and legend
        plt.xticks(size = figure_axes_text_size)
        plt.xlabel('time', size = figure_axes_text_size)
        plt.yticks(size = figure_axes_text_size)
        plt.ylabel('score', size = figure_axes_text_size)
        plt.title('Attack traces results', size = figure_axes_text_size)
        plt.legend(loc="best")
        
        #plot results in bar chart
        plt.subplot(1,2,2)        
        s = attack_object.scores[:, key_byte]
        plt.bar(range(len(s)),s, color=color_all_guesses)
        plt.bar(best_guesses[key_byte], s[best_guesses[key_byte]], color=color_best_guess) 
        if correct_key is not None:  
            plt.bar(correct_key[key_byte], s[correct_key[key_byte]], color=color_right_guess) 
        plt.ylim((np.min(s), np.max(s)))
        plt.xlabel("Key guesses")
        plt.ylabel("Scores")
        plt.show()

        # Plot convergence traces
        for i in range(guesses_number): plt.plot(attack_object.convergence_traces[i,key_byte,:].T, color = color_all_guesses)
        plt.plot(attack_object.convergence_traces[best_guesses[key_byte],key_byte,:].T, color = color_best_guess, label = 'best score')
        if correct_key is not None:  
            plt.plot(attack_object.convergence_traces[correct_key[key_byte],key_byte].T[:-1:DOWNS_STEP], color = color_right_guess, label = 'right key')
        # Set axes and legend
        plt.xlabel('traces number', size = figure_axes_text_size)
        plt.ylabel('score', size = figure_axes_text_size)
        plt.xticks(np.arange(0,CONV_POINTS, 1),np.arange(1,CONV_POINTS+1, 1)*(attack_object.convergence_step), size = figure_axes_text_size)
        plt.title('Convergence traces results', size = figure_axes_text_size)
        plt.yticks(size = figure_axes_text_size)
        plt.show()        
    
    else:      
        for i in range(guesses_number): plt.plot(attack_object.results[i,key_byte].T[:-1:DOWNS_STEP], color = color_all_guesses)
        plt.plot(attack_object.results[best_guesses[key_byte],key_byte].T[:-1:DOWNS_STEP], color = color_best_guess, label='best score')
        if correct_key is not None: 
            plt.plot(attack_object.results[correct_key[key_byte],key_byte].T[:-1:DOWNS_STEP], color = color_right_guess, label='right key')
        # Set axes and legend
        plt.xticks(size = figure_axes_text_size)
        plt.xlabel('time', size = figure_axes_text_size)
        plt.yticks(size = figure_axes_text_size)
        plt.ylabel('score', size = figure_axes_text_size)
        plt.title('Attack traces results', size = figure_axes_text_size)
        plt.legend(loc="best")
        plt.show()

    print("Best guess for byte "+str(key_byte)+" = " + hex(best_guesses[key_byte]))
    if correct_key is not None:     
        print("Correct guess for byte : "+str(key_byte)+"=" + hex(correct_key[key_byte]))
        
def plot_attack_result(attack_object, key_byte=None, correct_key=None):

    if key_byte is not None: 
        plt.rcParams["figure.figsize"] = [17, 3]
        plot_attack_result_single_byte(attack_object, key_byte, correct_key)
    else:
        plt.rcParams["figure.figsize"] = [14, 2]
        for byte_nb in range(attack_object.results.shape[1]):
            plot_attack_result_single_byte(attack_object, byte_nb, correct_key)

def print_attack_best_scores(attack, scores_number: int) -> None:
    """Display the best scores, in a notebook context.

    Args:
        attack: The attack object that has been run, and from which we extract scores.
        scores_number: The number of scores to display.
    """
    
    bytes_number = attack.scores.shape[1]   
    num_A_scores = np.nan_to_num(attack.scores)
    
    _display.display(_display.Markdown('__Best ' + str(scores_number)  + ' guesses for all key bytes__\n'))

    lines = []
    lines.append("Bytes")
    lines.append("------")
    lines.append("guess/score ")
    
    for byte_pos in range(bytes_number):
        best_scores = np.flip(np.argsort(num_A_scores[:, byte_pos], axis=0)[-scores_number:])
        
        lines[0] += "|" + str(byte_pos)
        lines[1] += "|--"
        
        for k in range(scores_number):        
            lines.append("guess/score ")
            lines[k+2] += "|("+str(hex(best_scores[k]))+f', {num_A_scores[best_scores[k], byte_pos]:.3f})'
    
    lines_display = lines[0] + "\n" + lines[1] + "\n"
    for i in range(scores_number):
        lines_display += lines[i+2] + "\n"
    
    _display.display(_display.Markdown(lines_display))     

def print_attack_result(attack, correct_key=None):
    """Display the best score per byte, in a notebook context.

    Args:
        attack: The attack object that has been run, and from which we extract scores.
    """
    
    bytes_number = attack.scores.shape[1]   
    num_A_scores = np.nan_to_num(attack.scores)

    _display.display(_display.Markdown('__Best guesses for all key bytes__\n'))

    lines = []
    lines.append("Bytes")
    lines.append("------")
    lines.append("guess ")
    lines.append("score ")
    lines.append("right key ")
    lines.append("rank ")
    
    for byte_pos in range(bytes_number):
        best_scores = np.flip(np.argsort(num_A_scores[:, byte_pos], axis=0)[-1:])
        lines[0] += "|" + str(byte_pos)
        lines[1] += "|--"
        lines[2] += "|"+hex(best_scores[0])
        lines[3] += f'|{num_A_scores[best_scores[0], byte_pos]:.5f}'
        if correct_key is not None: 
            lines[4] += "|"+hex(correct_key[byte_pos])
            rank_right_key = np.where(np.flip(np.argsort(num_A_scores[:, byte_pos], axis=0)) == correct_key[byte_pos])[0][0]+1
            lines[5] += "|"+str(rank_right_key)

    if correct_key is not None: 
        lines_display = lines[0] + "\n" + lines[1] + "\n" + lines[2] + "\n" + lines[3] + "\n" + lines[4] + "\n" + lines[5]
    else:
        lines_display = lines[0] + "\n" + lines[1] + "\n" + lines[2] + "\n" + lines[3]
    _display.display(_display.Markdown(lines_display))     
    

    

def plot_attack_ranks(attack, correct_key=None):

    if correct_key is not None: 
        plt.rcParams['figure.figsize']=(17,5)

        bytes_number = attack.scores.shape[1] 
        rank_list = np.zeros((bytes_number,attack.convergence_traces.shape[2]) ,dtype=np.uint16)

        for step in range(attack.convergence_traces.shape[2]):
            num_A_scores = np.nan_to_num(attack.convergence_traces[:,:,step])

            for byte_pos in range(bytes_number):
                rank_right_key = np.where(np.flip(np.argsort(num_A_scores[:, byte_pos], axis=0)) == correct_key[byte_pos])[0][0]+1
                rank_list[byte_pos][step] = rank_right_key

        CONV_POINTS =  attack.convergence_traces.shape[2]
        for i in range(bytes_number):
            plt.plot(rank_list[i].T, label="byte %d " %i)
        plt.legend(prop={'size': graph_title_fontsize}, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)      
        plt.title('Bytes rank evolution', size=graph_title_fontsize)
        plt.xlabel('traces number')
        plt.xticks(np.arange(0,CONV_POINTS, 1),np.arange(1,CONV_POINTS+1, 1)*(attack.convergence_step), size = graph_title_fontsize)
        plt.show()    
    else:
        print('correct key unknown')
    
    
    
    
    
    
    
    
            self.attack_object = attack_object
        self.attack_object_convergence_step = attack_object.convergence_step
        self.attack_object_convergence_traces = attack_object.convergence_traces
        self.attack_object_results = attack_object.results
        self.attack_object_scores = attack_object.scores
        self.attack_object_processed_traces =  attack_object.processed_traces
        self.figure_name_path = figure_name_path
        self.file_name_path = file_name_path
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
def remaining_entropy_naive(attack, correct_key):
    """Display the remaining entropy 
    Args:
        attack: The attack object that has been run, and from which we extract scores.
    """
    if attack.convergence_step is None:
        print('No convergence result available')
        return [[], []]

    plt.rcParams["figure.figsize"] = [20, 6]
    axes = plt.gca()

    bytes_number = attack.scores.shape[1]   
    guesses_number = attack.results.shape[0]
    maxLog = bytes_number*math.log2(guesses_number)
    entropy_min_list = [maxLog]
    entropy_max_list = [maxLog]

    for step in range(attack.convergence_traces.shape[2]):
        num_A_scores = np.nan_to_num(attack.convergence_traces[:,:,step])
        rank_list = np.zeros(bytes_number,dtype=np.uint16)

        entropy_min = 0
        for byte_pos in range(bytes_number):
            best_scores = np.flip(np.argsort(num_A_scores[:, byte_pos], axis=0)[-1:])
            rank_right_key = np.where(np.flip(np.argsort(num_A_scores[:, byte_pos], axis=0)) == correct_key[byte_pos])[0][0]+1
            rank_list[byte_pos] = rank_right_key
            entropy_min = entropy_min + math.log2(rank_right_key)

        entropy_max = math.log2(np.max(rank_list))*bytes_number

        entropy_min_list.append(entropy_min)
        entropy_max_list.append(entropy_max)

    entropy_mean_list = np.mean([np.array(entropy_min_list), np.array(entropy_max_list)], axis = 0)

    x1 = np.arange(0, attack.processed_traces, attack.convergence_step)
    x1 = np.hstack((x1,attack.processed_traces))
    y1 = np.array(entropy_min_list)
    x2 = x1
    y2 = np.array(entropy_max_list)
    y3 = entropy_mean_list

    line_32 = np.tile(32, len(x1))
    # Get abcisse when entropy is lower to 32 bits
    idx_mean = np.argwhere((entropy_mean_list-line_32)<0).flatten()    
    if (len(idx_mean) != 0):
        traces_mean = x1[idx_mean[0]]
    else:
        traces_mean = None

    idx_min = np.argwhere((entropy_min_list-line_32)<0).flatten()    
    if (len(idx_min) != 0):
        traces_min = x1[idx_min[0]]
    else:
        traces_min = None

    idx_max = np.argwhere((entropy_max_list-line_32)<0).flatten()    
    if (len(idx_max) != 0):
        traces_max = x1[idx_max[0]]
    else:
        traces_max = None    

    if 0 in entropy_mean_list:
        line_0 = np.tile(0, len(x1))
        idx_success = np.argwhere((entropy_max_list-line_0)==0).flatten()[0]
        traces_success = x1[idx_success]
    else:
        traces_success = None      

    axes.set_xlabel('Number of traces')
    axes.set_ylabel('Key remaining entropy, log2')
    plt.plot(x1, y1, color = 'green', label='best entropy')
    plt.plot(x1, y2, color = 'black', label='worse entropy')
    plt.plot(x1, y3, color = 'red', label='mean entropy')    
    plt.plot(x1, line_32, '--', color = 'black', label='2^32')    
    plt.xlim(0)    
    plt.ylim(0)
    plt.legend()
    plt.title('Guessing Entropy Graph', fontsize = 14)

    plt.fill(
        np.append(x1, x2[::-1]),
        np.append(y1, y2[::-1]),
    )        
    print('-----------------------------------------------------------')    
    print('Number of traces for full key recovery            = ',traces_success)
    print('-----------------------------------------------------------')    
    print('Number of traces for 32-bit remaining max-entropy  = ',traces_max)
    print('Number of traces for 32-bit remaining min-entropy  = ',traces_min)
    print('Number of traces for 32-bit remaining mean-entropy = ',traces_mean)
    print('-----------------------------------------------------------')

    return entropy_min_list, entropy_max_list, entropy_mean_list

def print_template_attack_result(attack_list, correct_key=None):
    """Display the best score per byte, in a notebook context.

    Args:
        attack: The attack object that has been run, and from which we extract scores.
    """
    bytes_number = len(attack_list)  
  
    _display.display(_display.Markdown('__Best guesses for all key bytes__\n'))

    lines = []
    lines.append("Bytes")
    lines.append("------")
    lines.append("guess ")
    lines.append("score ")
    lines.append("right key ")
    lines.append("rank ")
    
    for byte_pos in range(len(attack_list)):
        attack = attack_list[byte_pos]
        num_A_scores = np.nan_to_num(attack.scores)
        best_scores = np.flip(np.argsort(num_A_scores, axis=0)[-1:])[0]
        lines[0] += "|" + str(byte_pos)
        lines[1] += "|--"
        lines[2] += "|"+hex(best_scores)
        lines[3] += f'|{num_A_scores[best_scores]:.5f}'
        if correct_key is not None: 
            lines[4] += "|"+hex(correct_key[byte_pos])
            rank_right_key = np.where(np.flip(np.argsort(num_A_scores, axis=0)) == correct_key[byte_pos])[0][0]+1
            lines[5] += "|"+str(rank_right_key)

    if correct_key is not None: 
        lines_display = lines[0] + "\n" + lines[1] + "\n" + lines[2] + "\n" + lines[3] + "\n" + lines[4] + "\n" + lines[5]
    else:
        lines_display = lines[0] + "\n" + lines[1] + "\n" + lines[2] + "\n" + lines[3]
    _display.display(_display.Markdown(lines_display))     
    
def plot_template_attack_result(attack_list, right_key):
    plt.rcParams['figure.figsize']=(15, 2)

    for word in range(len(attack_list)):    
        # Plot the scores
        T = attack_list[word]
        s = T.scores.squeeze()   

        plt.subplot(121)
        plt.bar(range(len(s)), s, color=color_all_guesses)
        plt.bar(right_key[word], s[right_key[word]], color=color_right_guess) 
        plt.ylim((np.min(s), np.max(s)))
        plt.xlabel("Key guesses")
        plt.ylabel("Scores")
        plt.title("Templates Scores: Byte %d"%(word))

        # You can also visualize scores increasing with the number of matching traces
        x = np.arange(0, T.processed_traces, T.convergence_step) + T.convergence_step
        c = T.convergence_traces.squeeze()
        c = c - c.mean(0)
        
        plt.subplot(122)
        plt.plot(x, c.T, color = color_all_guesses)
        plt.plot(x, c[right_key[word]], color = color_right_guess)
        plt.xlabel("Number of traces")
        plt.ylabel("Scores")
        plt.title("Convergence: Byte %d"%(word))

        plt.show()
    
def template_attack_entropy(attack_list, correct_key):
    """Display the remaining entropy 
    Args:
        attack: The attack object that has been run, and from which we extract scores.
    """
    plt.rcParams["figure.figsize"] = [20, 5]
    axes = plt.gca()
    
    bytes_number = len(attack_list)
    attack = attack_list[0]
    guesses_number = attack.results.shape[0]
    maxLog = bytes_number*math.log2(guesses_number)
    entropy_min_list = [maxLog]
    entropy_max_list = [maxLog]
    for step in range(attack.convergence_traces.shape[1]):

        entropy_min = 0
        for byte in range(bytes_number):
            attack = attack_list[byte]
            if attack.convergence_step is None:
                print('No convergence result available')
                return [[], []]

            num_A_scores = np.nan_to_num(attack.convergence_traces[:,step])
            rank_list = np.zeros(bytes_number,dtype=np.uint16)
            rank_right_key = np.where(np.flip(np.argsort(num_A_scores, axis=0)) == correct_key[byte])[0][0]+1
            rank_list[byte] = rank_right_key
            entropy_min = entropy_min + math.log2(rank_right_key)

        entropy_max = math.log2(np.max(rank_list))*bytes_number
        entropy_min_list.append(entropy_min)
        entropy_max_list.append(entropy_max)
        
    x1 = np.arange(0, attack.processed_traces, attack.convergence_step)
    x1 = np.hstack((x1,attack.processed_traces))
    y1 = np.array(entropy_min_list)
    x2 = x1
    y2 = np.array(entropy_max_list)
    axes.set_xlabel('Number of traces')
    axes.set_ylabel('Key remaining entropy, log2')
    
    
    plt.plot(x1, y1, color = 'black', label='best entropy')
    plt.plot(x2, y2, color = 'red', label='worse entropy')
    plt.ylim(0, maxLog)
    plt.xlim(0)
    plt.legend()
    plt.title('Guessing Entropy Graph', fontsize = 14)

    plt.fill(
        np.append(x1, x2[::-1]),
        np.append(y1, y2[::-1]),
    )        
    
    return entropy_min_list, entropy_max_list

   
"""
RankEstimation implements an algorithm proposed here https://eprint.iacr.org/2014/920.pdf
It takes as an input an array p of probabilities for each engine and guess,
the real key and a parameter binWidth, controling the accuracy of the estimation.
It outputs the lower bound, estimated rank and upper bound
:param p: probabilities of each guess and engines
:param key_real: the real key
:param binWidth: parameter controlling the accuracy
:return: (lower bound, estimated rank, upper bound)

"""
def RankEstimation(p, key_real, binWidth):
        
    q=np.log(p)
    q=np.nan_to_num(q,neginf=-100)# requires numpy version 1.17 or newer!!! but makes the algorithm more stable
    subkeyNum = p.shape[0]
    histMin = 0
    y = np.array(1, dtype=np.float64)
    #Convolve the histograms
    for subkeyNo in range(subkeyNum):
        maxi, mini = np.max(q[subkeyNo]), np.min(q[subkeyNo])
        bins = max(int(np.ceil((maxi-mini)/binWidth)),1)
        maxi = mini + bins*binWidth #ensures equal binsize across histograms
        hist, edges = np.histogram( q[subkeyNo], bins=bins, range=(mini,maxi))
        histMin = histMin + edges[0]
        y = np.convolve(y, hist)
    #calculate bin number of the real key
    binNoReal = 0
    for subkeyNo in range(subkeyNum):
        candNo = key_real[subkeyNo]
        binNoReal = binNoReal + q[subkeyNo, candNo]
    binNoReal = int(( binNoReal - histMin ) / binWidth)

    binNoMax = max(0,binNoReal-subkeyNum)
    keyRankMax = np.sum(y[binNoMax:])

    binNoMin = binNoReal+subkeyNum
    keyRankMin = np.sum(y[binNoMin:])

    binNoEst = binNoReal
    keyRankEst = np.sum(y[binNoEst:])

    return keyRankMin, keyRankEst, keyRankMax


def remaining_entropy(attack, correct_key):
    """Display the remaining entropy 
    Args:
        attack: The attack object that has been run, and from which we extract scores.
    """
    if attack.convergence_step is None:
        print('No convergence result available')
        return [[], []]

    plt.rcParams["figure.figsize"] = [20, 6]
    axes = plt.gca()

    bytes_number = attack.scores.shape[1]   
    guesses_number = attack.results.shape[0]
    maxLog = bytes_number*math.log2(guesses_number)
    key_rank_lower = [maxLog]
    key_rank_max = [maxLog]
    key_rank_est = [maxLog]

    for step in range(attack.convergence_traces.shape[2]):
        scores = np.nan_to_num(attack.convergence_traces[:,:,step]).T
        scores.shape
        #in case that all scores have value 0 for an engine, add a constant,
        #so normalizaion won't fail
        for i in range(scores.shape[0]):
            if np.all(scores[i]==0):
                scores[i]+=1

        probabilities = np.nan_to_num(scores/np.expand_dims(scores.sum(1),1))

        rank_est = RankEstimation(probabilities, correct_key, 0.005)
#        rank_est = RankEstimation(probabilities, correct_key, 0.02)


        key_rank_lower.append(math.log2(rank_est[0]+1))
        key_rank_est.append(math.log2(rank_est[1]+1))
        key_rank_max.append(math.log2(rank_est[2]+1))

    # Plot all results
    x1 = np.arange(0, attack.processed_traces, attack.convergence_step)
    x1 = np.hstack((x1,attack.processed_traces))
    y1 = np.array(key_rank_lower)
    x2 = x1
    y2 = np.array(key_rank_max)
    y3 = key_rank_est

    line_32 = np.tile(32, len(x1))
    # Get abcisse when entropy is lower to 32 bits
    idx_est = np.argwhere((key_rank_est-line_32)<0).flatten()    
    if (len(idx_est) != 0):
        traces_est = x1[idx_est[0]]
    else:
        traces_est = None

    idx_lower = np.argwhere((key_rank_lower-line_32)<0).flatten()    
    if (len(idx_lower) != 0):
        traces_lower = x1[idx_lower[0]]
    else:
        traces_lower = None

    idx_max = np.argwhere((key_rank_max-line_32)<0).flatten()    
    if (len(idx_max) != 0):
        traces_max = x1[idx_max[0]]
    else:
        traces_max = None    

    if 0 in key_rank_est:
        line_0 = np.tile(0, len(x1))
        idx_success = np.argwhere((key_rank_est-line_0)==0).flatten()[0]
        traces_success = x1[idx_success]
    else:
        traces_success = None      

    axes.set_xlabel('Number of traces')
    axes.set_ylabel('Key remaining entropy, log2')
    plt.plot(x1, line_32, '--', color = 'black', label='2^32')    
    plt.plot(x1, y1, color = 'green', label='rank ge lower bound')
    plt.plot(x1, y2, color = 'black', label='rank ge higher bound')
    plt.plot(x1, y3, color = 'red', label='rank ge estimated entropy')    
    plt.xlim(0)    
    plt.ylim(0)
    plt.legend()
    plt.title('Guessing Entropy Graph', fontsize = 14)

    plt.fill(
        np.append(x1, x2[::-1]),
        np.append(y1, y2[::-1]),
        color = 'lightgreen'
    )    
        
    print('-----------------------------------------------------------')    
    print('Number of traces for full key recovery            = ',traces_success)
    print('-----------------------------------------------------------')    
    print('Number of traces for 32-bit remaining entropy: ')
    print('-- Higher bound entropy  = ',traces_max)
    print('-- Lower bound entropy   = ',traces_lower)
    print('-- Estimated entropy     = ',traces_est)
    print('-----------------------------------------------------------')

    return key_rank_lower, key_rank_est, key_rank_max


