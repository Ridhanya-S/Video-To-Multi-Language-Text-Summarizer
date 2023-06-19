import matplotlib.pyplot as plt
import numpy as np
import json
from rouge import Rouge
from download import text_file_convert

# SCORE - JSON FILE
def eval_scores(reference,prediction,output_path):
    rouge = Rouge()
    tot_scores = rouge.get_scores(prediction, reference)
    scores = tot_scores[0]['rouge-l']
    # data = sc(scores)
    data = json.dumps([{'Metric': metr, 'Score': sc} for metr, sc in scores.items()], indent=4)
    with open(f'{output_path}/_eval_scores.json', 'w') as f:
        f.write(data)

    return scores


def piechart(scores, metrics,output_path):
  myexplode = [0.02, 0.02, 0.02]
  fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(aspect="equal"))
  sc,texts,autotexts = plt.pie(list(scores.values()), labels = metrics, explode = myexplode, shadow = False,autopct='%1.1f%%', startangle=90)
  plt.setp(autotexts, size=12, weight="bold",color = 'white')
  plt.legend(loc ="best", labelcolor='linecolor')
  ax.set_title("Distribution of performance metrics: A pie chart",size=15)
  plt.savefig(f'{output_path}/piechart.png')
  plt.show() 


def barplot(metrics, scores, output_path):
  plt.figure(figsize = (10,6))
  plt.bar(metrics,list(scores.values()), width= 0.5, align='center',color='slateblue')
  plt.title("Bar plot representing the scores by the performance metrics", fontsize=15)
  plt.xlabel('Metrics', fontsize=12)
  plt.ylabel('Scores', fontsize=12)
  plt.savefig(f'{output_path}/barplot.png')
  plt.show()

def compare_final_summary(reference,prediction_bart,prediction_rb,output_path):
  metrics = ['recall','precision','f1 score']
  sc_bart = eval_scores(reference,prediction_bart,output_path)
  print(sc_bart)
  sc_rb = eval_scores(reference,prediction_rb,output_path)
  print(sc_rb)
  barWidth = 0.25
  fig = plt.subplots(figsize =(8, 6))

  precision = []
  pbart = sc_bart['p']
  prb = sc_rb['p']
  precision.append(pbart)
  precision.append(prb)

  recall = []
  rbart = sc_bart['r']
  rrb = sc_rb['r']
  recall.append(rbart)
  recall.append(rrb)

  f1 = []
  fbart = sc_bart['f']
  frb = sc_rb['f']
  f1.append(fbart)
  f1.append(frb)

  # Set position of bar on X axis
  br1 = np.arange(len(precision))
  br2 = [x + barWidth for x in br1]
  br3 = [x + barWidth for x in br2]

  # Make the plot
  plt.bar(br1, precision, color ='r', width = barWidth,edgecolor ='grey', label ='Precision')
  plt.bar(br2, recall, color ='g', width = barWidth,edgecolor ='grey', label ='Recall')
  plt.bar(br3, f1, color ='b', width = barWidth,edgecolor ='grey', label ='F1 Score')

  # Adding Xticks
  plt.xlabel('MODELS')
  plt.ylabel('METRICS SCORES')
  plt.xticks([r + barWidth for r in range(len(precision))],['BART','SIMILARITY SCORE'])
  plt.savefig(f'{output_path}/comparison_plot.png')
  plt.legend()
  plt.savefig(f'{output_path}/comparison_plot.png')
  plt.show()

  pre1 = sc_bart['p'] 
  pre2 = sc_rb['p']

  if (pre1 > pre2):
    print("\nMODEL SELECTED : BART")
    # final_summary = summarizer_bart(text,output_path)
    text_file_convert(prediction_bart, "final_text_summary", output_path) 
    piechart(sc_bart, metrics,output_path)
    barplot(metrics, sc_bart, output_path)
    sc_bart = eval_scores(reference,prediction_bart,output_path)
    return prediction_bart
  
  # elif ((sc_bart['r'] > sc_rb['r']) and (sc_bart['f'] > sc_rb['f'])):

  else:
    print("\nMODEL SELECTED : SPACY MODEL")
    # final_summary = summarizer_rb(text,file_path)
    text_file_convert(prediction_rb, "final_text_summary", output_path)
    piechart(sc_rb, metrics,output_path)
    barplot(metrics, sc_rb, output_path)
    sc_rb = eval_scores(reference,prediction_bart,output_path)
    return prediction_rb

  