from sql_app.crud import getDocsForTerm, getSongIds, getDocumentsInLinkedList
from sql_app.database import SessionLocal

BooleanOperator = {'AND', 'OR', 'NOT', 'and', 'or', 'not'}


def getAllDocumentIDs():
    db = SessionLocal()
    foundIds = getSongIds(db)
    foundIds.sort()
    return foundIds


def operatorAND(list1, list2):
    answer = []
    index1 = 0
    index2 = 0
    while index1 < len(list1) and index2 < len(list2):
        if list1[index1] < list2[index2]:
            index1 += 1
        elif list1[index1] > list2[index2]:
            index2 += 1
        else:
            answer.append(list1[index1])
            index1 += 1
            index2 += 1
    return answer


def operatorOR(list1, list2):
    answer = []
    index1 = 0
    index2 = 0
    while index1 < len(list1) and index2 < len(list2):
        if list1[index1] < list2[index2]:
            answer.append(list1[index1])
            index1 += 1
        elif list1[index1] > list2[index2]:
            answer.append(list2[index2])
            index2 += 1
        else:
            answer.append(list1[index1])
            index1 += 1
            index2 += 1

    if index1 < len(list1):
        answer = answer + list1[index1:]
    if index2 < len(list2):
        answer = answer + list2[index2:]
    return answer


def operatorNOT(list1):
    answer = []
    list2 = getAllDocumentIDs()
    index1 = 0
    index2 = 0
    while index1 < len(list1) and index2 < len(list2):
        if list1[index1] < list2[index2]:
            index1 += 1
        elif list1[index1] > list2[index2]:
            answer.append(list2[index2])
            index2 += 1
        else:
            index1 += 1
            index2 += 1

    if index2 < len(list2):
        answer = answer + list2[index2:]
    return answer


# Query Filtration
# input : Query
# output : List of terms of a given query which mach with the terms in our datafiles
def QueryFiltration(expression):
    QTerms = []

    # Add spaces next to brackets if they are not present in the input expression.
    expression = expression.replace("(", " ( ").replace(")", " ) ")
    Q = expression.lower().split()
    for Qterm in Q:
        QTerms.append(Qterm)
    return QTerms


# Convert a boolean expression from infix to prefix notation.
def convertInfixToPrefix(expression):
    # Define operator precedence
    expression = QueryFiltration(expression)
    precedence = {"not": 3, "and": 2, "or": 1}
    stack = []
    output = []
    for token in reversed(expression):
        if token == ")":
            stack.append(token)
        elif token == "(":
            while stack[-1] != ")":
                output.append(stack.pop())
            stack.pop()
        elif token in precedence:
            while (stack and stack[-1] != ")" and
                   precedence[token] < precedence[stack[-1]]):
                output.append(stack.pop())
            stack.append(token)
        else:
            output.append(token)
    while stack:
        output.append(stack.pop())
    return list(reversed(output))


def parseQuery(q, index):
    term = q[index]
    if term == 'and':
        answer1, id_rest = parseQuery(q, index + 1)
        answer2, id_rest = parseQuery(q, id_rest)
        answer = operatorAND(answer1, answer2)
        return answer, id_rest
    elif term == 'or':
        answer1, id_rest = parseQuery(q, index + 1)
        answer2, id_rest = parseQuery(q, id_rest)
        answer = operatorOR(answer1, answer2)
        return answer, id_rest
    elif term == 'not':
        answer, id_rest = parseQuery(q, index + 1)
        answer = operatorNOT(answer)
        return answer, id_rest
    else:
        db = SessionLocal()
        # For invertedList implementation
        answer = getDocumentsInLinkedList(db, term)
        # For simple search implementation
        # answer = getDocsForTerm(db, term)
        return answer, index + 1


# input : Query - war AND (bullet or not friend)
# output : list of ids, that satisfy given expression
def retrieveDocumentIds(expression):
    expression = convertInfixToPrefix(expression)
    answer, ind = parseQuery(expression, 0)
    return answer
