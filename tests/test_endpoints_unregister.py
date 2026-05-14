def test_unregister_existing_participant(client, sample_activity, sample_email):
    # Arrange
    signup_url = f"/activities/{sample_activity}/signup?email={sample_email}"
    unregister_url = f"/activities/{sample_activity}/signup?email={sample_email}"
    client.post(signup_url)

    # Act
    response = client.delete(unregister_url)
    activities_response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Unregistered {sample_email} from {sample_activity}"}
    participants = activities_response.json()[sample_activity]["participants"]
    assert sample_email not in participants


def test_unregister_nonexistent_activity_returns_404(client, sample_email):
    # Arrange
    unregister_url = f"/activities/Unknown%20Club/signup?email={sample_email}"

    # Act
    response = client.delete(unregister_url)

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_missing_participant_returns_404(client, sample_activity, sample_email):
    # Arrange
    unregister_url = f"/activities/{sample_activity}/signup?email={sample_email}"

    # Act
    response = client.delete(unregister_url)

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found"
