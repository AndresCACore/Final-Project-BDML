# Final_Project 🚀

## **CAR BLACK BOX**  :orange_square:

### (:eye_speech_bubble: FATIGUE DETECTION :zzz:) 


The idea of the project is to be able to recognize the gestures of tiredness or drowsiness in people who may fall asleep in inappropriate situations or moments, for example while driving. 

The objective is to recognize when the driver of a vehicle starts yawning or blinking frequently. 

#### **The Drowsy Driving Problem**
This usually happens when a driver has not slept enough, but it can also happen because of untreated sleep disorders, medications, drinking alcohol, or shift work
- Makes you less able to pay attention to the road.
- Slows reaction time if you must brake or steer suddenly.
- Affects your ability to make good decisions.


<p align="center">
  <img width="460" height="200" src="http://www.thedetroitbureau.com/wp-content/uploads/2013/01/Drowsy-Driving.jpg">
</p>




---
# Steps :white_check_mark:

<center>

| 1 STEP  | 2 STEP | 3 STEP  | 4 STEP | 5 STEP | 6 STEP |
|------|:------:|:------:|:------:|:------:|:------:|
| Search Dataset  | Web Scraping | Clear data | Create drowsiness dataset | Train ML  | Interface PyQt 5 |

</center>

```mermaid
graph TD;
    1-->3;
    2-->3;
    3-->4;
    4-->5;
    5-->6;
```

## Related articles 📋
---
- https://arxiv.org/pdf/2112.10298.pdf
- https://iopscience.iop.org/article/10.1088/1742-6596/1090/1/012037/pdf
- https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8716716
- https://repositorio.upct.es/xmlui/bitstream/handle/10317/7793/tfg-gar-des.pdf?sequence=1&isAllowed=y

## DATASET 📦
---
- Driver drowsiness 
  - [Photos](https://www.kaggle.com/dheerajperumandla/drowsiness-dataset)

- Driver drowsines 
  - [Videos](http://vlm1.uta.edu/~athitsos/projects/drowsiness/?C=M;O=A)

- Cohn-kanade dataset 
  - [Emotion recognition](https://github.com/spenceryee/CS229/tree/master/CK%2B)

- DrowsyDriverDetection
  - [Photos](https://github.com/nishagandhi/DrowsyDriverDetection/tree/master/data/testing/Alert)

---
## Models :construction:
- Supervised Learning Classification
Model:
- Loss: 0.0875
- Accuracy: 0.96 
<p align="center">
  <img width="360" height="700" src="/Data/img/firts_model.png">
</p>
<p align="center">
  <img width="460" height="200" src="/Data/img/firts_model_accuracy.png">
</p>
<p align="center">
  <img width="460" height="200" src="/Data/img/firts_model_loss.png">
</p>

## RESULTS
---
### Positive Results
- Results of fatigue recognition at close range (approximately 45 cm from the camera)

 - Without glasses

<p align="center">
  <img width="460" height="300" src="img/neard.jpg">
</p>

 - With glasses

<p align="center">
  <img width="460" height="300" src="img/neard_glass.jpg">
</p>

### Negative Results
- Results of fatigue recognition at long distance (approximately 85 cm from the camera).

 - If several errors occur in face recognition due to distance, the recognition efficiency decreases considerably. 

<p align="center">
  <img width="460" height="200" src="img/fail.jpg">
</p>

### Save Results

<p align="center">
  <img width="460" height="200" src="img/records.jpg">
</p>

### Interface

<p align="center">
  <img width="460" height="200" src="img/results.jpg">
</p>


### Conclusions 
- :white_check_mark: Facial recognition metrics improve the closer you are to the camera, and ambient lighting must also be taken into account. 

- :x: Results vary when the user is wearing accessories (glasses or mask). 

- :x: Results are not optimal for users with beards.

## REQUERIMENTS 🛠️
---
<p align="center">
  <img width="360" height="100" src="img/tensorflow.png">
</p>

<p align="center">
  <img width="350" height="50" src="img/keras.png">
</p>

<p align="center">
  <img width="460" height="200" src="img/opencv.png">
</p>
<p align="center">
  <img width="360" height="100" src="img/dlib.jpeg">
</p>

<p align="center">
  <img width="330" height="100" src="img/pyqt.png">
</p>


## Autor ✒️
  - Andrés Carvajal
 <a href="https://www.linkedin.com/in/pablo-andr%C3%A9s-carvajal-andrade-a96897171/" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/linkedin.svg" alt="carlos salvador díaz" height="30" width="40" />linkedin</a>
---
