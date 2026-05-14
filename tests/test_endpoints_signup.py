def test_signup_successfully_adds_participant(client, sample_activity, sample_email):
    # Arrange
    signup_url = f"/activities/{sample_activity}/signup?email={sample_email}"

    # Act
    response = client.post(signup_url)
    activities_response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {sample_email} for {sample_activity}"}
    participants = activities_response.json()[sample_activity]["participants"]
    assert sample_email in participants


def test_signup_nonexistent_activity_returns_404(client, sample_email):
    # Arrange
    signup_url = f"/activities/Unknown%20Club/signup?email={sample_email}"

    # Act
    response = client.post(signup_url)

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_duplicate_participant_returns_409(client, sample_activity, sample_email):
    # Arrange
    signup_url = f"/activities/{sample_activity}/signup?email={sample_email}"
    client.post(signup_url)

    # Act
    duplicate_response = client.post(signup_url)

    # Assert
    assert duplicate_response.status_code == 409
    assert duplicate_response.json()["detail"] == "Participant already signed up"
