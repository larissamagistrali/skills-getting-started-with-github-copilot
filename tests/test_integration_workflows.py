def test_signup_then_unregister_workflow(client, sample_activity, sample_email):
    # Arrange
    signup_url = f"/activities/{sample_activity}/signup?email={sample_email}"
    unregister_url = f"/activities/{sample_activity}/signup?email={sample_email}"

    # Act
    signup_response = client.post(signup_url)
    after_signup = client.get("/activities").json()[sample_activity]["participants"]
    unregister_response = client.delete(unregister_url)
    after_unregister = client.get("/activities").json()[sample_activity]["participants"]

    # Assert
    assert signup_response.status_code == 200
    assert sample_email in after_signup
    assert unregister_response.status_code == 200
    assert sample_email not in after_unregister


def test_same_email_can_signup_in_different_activities(client, sample_email):
    # Arrange
    first_activity = "Chess Club"
    second_activity = "Robotics Team"

    # Act
    first_response = client.post(f"/activities/{first_activity}/signup?email={sample_email}")
    second_response = client.post(f"/activities/{second_activity}/signup?email={sample_email}")
    activities_payload = client.get("/activities").json()

    # Assert
    assert first_response.status_code == 200
    assert second_response.status_code == 200
    assert sample_email in activities_payload[first_activity]["participants"]
    assert sample_email in activities_payload[second_activity]["participants"]
