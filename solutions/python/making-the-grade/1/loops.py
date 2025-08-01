import math


def round_scores(student_scores):
  roundedScores = []
  for score in student_scores:
      roundedScores.append(round (score))
  return roundedScores


def count_failed_students(student_scores):
    count = 0
    for score in student_scores:
        if score <= 40:
            count += 1
    return count


def above_threshold(student_scores, threshold):
    bestScores = []
    for score in student_scores:
        if score >= threshold:
            bestScores.append(score)
    return bestScores


def letter_grades(highest):
    gradeBoundaries = []
    lowest = 41
    boundarySize = (highest - lowest) / 4
    for n in range (1, 5):
        boundary = math.ceil(highest - (boundarySize * n))
        print (highest - (boundarySize * n))
        gradeBoundaries.insert(0, boundary)
    return gradeBoundaries


def student_ranking(student_scores, student_names):
    rankings = []
    for name in student_names:
        entry = str(student_names.index(name) + 1) + '. ' + name + ': ' + str(student_scores[student_names.index(name)])
        rankings.append(entry)

    return rankings


def perfect_score(student_info):
    for student in student_info:
        if student[1] == 100:
            return student
    return []
