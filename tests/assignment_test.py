from core.models.assignments import Assignment

def test_correct_assignment_id(client, assignment_id):
    assignment = Assignment.get_by_id(assignment_id)
    Id = str(assignment).split()[1][0]
    assert Id == assignment_id


    