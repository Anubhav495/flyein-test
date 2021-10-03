from core.models.assignments import Assignment,AssignmentStateEnum
def test_get_assignments_student_1(client, h_student_1):
    response = client.get(
        '/student/assignments',
        headers=h_student_1
    )

    assert response.status_code == 200

    data = response.json['data']
    for assignment in data:
        assert assignment['student_id'] == 1


def test_get_assignments_student_2(client, h_student_2):
    response = client.get(
        '/student/assignments',
        headers=h_student_2
    )

    assert response.status_code == 200

    data = response.json['data']
    for assignment in data:
        assert assignment['student_id'] == 2


def test_post_assignment_student_1(client, h_student_1):
    content = 'ABCD TESTPOST'

    response = client.post(
        '/student/assignments',
        headers=h_student_1,
        json={
            'content': content
        })

    assert response.status_code == 200

    data = response.json['data']
    assert data['content'] == content
    assert data['state'] == AssignmentStateEnum.DRAFT
    assert data['teacher_id'] is None

def test_post_assignment_student_2(client, h_student_2):
    content = 'ABCD TESTPOST12'

    response = client.post(
        '/student/assignments',
        headers=h_student_2,
        json={
            'content': content
        })

    assert response.status_code == 200

    data = response.json['data']
    assert data['content'] == content
    assert data['state'] == AssignmentStateEnum.DRAFT
    assert data['teacher_id'] is None


'''added'''
def test_update_assignment_student_1(client, h_student_1):
    """
    [checks conditions for updating the assignment]
    """
    content = 'ABCD TESTPOST UPDATED'
    assignment_id=2
    assignment = Assignment.get_by_id(assignment_id)
    response = client.post(
        '/student/assignments',
        headers=h_student_1,
        json={
            'id': assignment_id, 
            'content': content
        })

    assert str(assignment).split()[1][0] == str(assignment_id)

    if assignment.state != AssignmentStateEnum.DRAFT:
        assert response.json['error'] == 'FyleError'
        assert response.status_code == 400
    else:
        assert response.status_code == 200
        data = response.json['data']
        assert data['content'] == content
        assert data['state'] == AssignmentStateEnum.DRAFT
        assert data['teacher_id'] is None

'''added'''
def test_submit_assignment_student_1(client, h_student_1):
    """
    [checks conditions for submitting the assignment]
    """
    response = client.post(
        '/student/assignments/submit',
        headers=h_student_1,
        json={
            'id': 2,
            'teacher_id': 2
        })
    if response.status_code == 400:
        data = response.json
        assert data['error'] == "FyleError"
    else:
        assert response.status_code == 200
        data = response.json['data']
        assert data['student_id'] == 1
        assert data['state'] == AssignmentStateEnum.SUBMITTED
        assert data['teacher_id'] == 2

'''added'''
def test_submit_assignment_student_2(client, h_student_2):
    """
    [checks conditions for submitting the assignment]
    """
    response = client.post(
        '/student/assignments/submit',
        headers=h_student_2,
        json={
            'id': 2,
            'teacher_id': 3
        })
    if response.status_code == 400:
        data = response.json
        assert data['error'] == "FyleError"
    else:
        assert response.status_code == 200
        data = response.json['data']
        assert data['student_id'] == 1
        assert data['state'] == AssignmentStateEnum.SUBMITTED
        assert data['teacher_id'] == 3

'''added'''
def test_empty_submit(client, h_student_2_custom):
    """
    [checks conditions for submitting an empty assignment]
    """
    content = ''
    response = client.post(
        '/student/assignments/submit',
        headers=h_student_2_custom,
        json={
            'id' : 233,
            'teacher_id': 2
        })

    assert response.status_code == 400

    assert response.json['error'] == 'FyleError'
    assert response.json['message'] == 'assignment with empty content cannot be submitted'




    
    
    
    
    

