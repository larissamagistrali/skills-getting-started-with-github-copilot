def test_activity_name_is_case_sensitive(client, sample_email):
    # Arrange
    signup_url = f"/activities/chess%20club/signup?email={sample_email}"

    # Act
    response = client.post(signup_url)

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_accepts_plus_alias_email(client, sample_activity):
    # Arrange
    alias_email = "student+club@example.com"
    signup_url = f"/activities/{sample_activity}/signup"

    # Act
    response = client.post(signup_url, params={"email": alias_email})
    participants = client.get("/activities").json()[sample_activity]["participants"]

    # Assert
    assert response.status_code == 200
    assert alias_email in participants
