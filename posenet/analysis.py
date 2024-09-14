import math
import cv2
import numpy as np

import posenet.constants

def angle_p_calculation(p1, p2, p3):
    v1 = ((p1[0]-p2[0]),(p1[1]-p2[1]))
    v2 = ((p3[0]-p2[0]),(p3[1]-p2[1]))
    v1_dot_v2 = (v1[0] * v2[0]) + (v1[1] * v1[1])
    denomonator = ((((v1[0]**2)+(v1[1]**2))**0.5)*(((v2[0]**2)+(v2[1]**2))**0.5))
    print(denomonator)
    theta = math.acos(v1_dot_v2/denomonator)
    return theta

def head_analysis(nose_C,sholder_L,sholder_R):
    sholder_C = ((sholder_L[0] + sholder_R[0])/2, (sholder_L[1] + sholder_R[1])/2)
    return (angle_p_calculation(nose_C, sholder_C, sholder_L), angle_p_calculation(nose_C, sholder_C, sholder_R))   


def form_angle_analysis(form_cord):
    form_angles = [0]*9#head1, head2, elbow1, pit1, elbow2, pit2, inLeg1, inLeg2, legPit1, legPit2
    part_dict = {"nose":form_cord[0], "leftEye":form_cord[1], "rightEye":form_cord[2], "leftEar":form_cord[3],
        "rightEar":form_cord[4], "leftShoulder":form_cord[5], "rightShoulder":form_cord[6], "leftElbow":form_cord[7],
        "rightElbow":form_cord[8], "leftWrist":form_cord[9], "rightWrist":form_cord[10], "leftHip":form_cord[11],
        "rightHip":form_cord[12], "leftKnee":form_cord[13], "rightKnee":form_cord[14], "leftAnkle":form_cord[15],
        "rightAnkle":form_cord[16]}
    form_angles[0], form_angles[1] = head_analysis(part_dict["nose"], part_dict["leftShoulder"],part_dict["rightShoulder"])
    form_angles[2] = head_analysis(part_dict["leftShoulder"], part_dict["leftElbow"],part_dict["leftWrist"])
    form_angles[3] = head_analysis(part_dict["leftHip"], part_dict["leftShoulder"],part_dict["leftElbow"])
    form_angles[4] = head_analysis(part_dict["rightShoulder"], part_dict["rightElbow"],part_dict["rightWrist"])
    form_angles[5] = head_analysis(part_dict["rightHip"], part_dict["rightShoulder"],part_dict["rightElbow"])
    form_angles[6] = head_analysis(part_dict["rightHip"], part_dict["leftHip"],part_dict["leftKnee"])
    form_angles[7] = head_analysis(part_dict["leftHip"], part_dict["rightHip"],part_dict["rightKnee"])
    form_angles[8] = head_analysis(part_dict["leftHip"], part_dict["leftKnee"],part_dict["leftAnkle"])
    form_angles[9] = head_analysis(part_dict["rightHip"], part_dict["rightKnee"],part_dict["rightAnkle"])
    return form_angles
    #@TODO needs to acount for vereation in size of the form_cord
def comparision(form_angle, perfect_angle):
    perfection_diff = []
    for I in range(len(form_angle)):
        perfection_diff.append(perfect_angle[I] - form_angle[I])
    return perfection_diff

def find_max_index(nums):
    if not nums:  # Check if the list is empty
        return None  # Return None for empty lists
    max_value = max(nums)  # Find the maximum value in the list
    max_index = nums.index(max_value)  # Find the index of the maximum value
    return max_index



def generate_feedback(form_cord, perfect_angle):
    perfection_diff = comparision(form_angle_analysis(form_cord), perfect_angle)
    max_error_index = find_max_index(perfection_diff)
    #generate the response using what this says. 
    



    

    
