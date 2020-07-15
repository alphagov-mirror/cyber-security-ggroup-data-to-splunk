# import filecmp
import os
import sys

import vcr

currentdir = os.path.dirname(__file__)
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


import script  # noqa: E402


@vcr.use_cassette
def test_get_scope():
    assert script.get_scope("/test_param/groups_scope") == [
        "https://www.test.groups.scope"
    ]


@vcr.use_cassette
def test_get_subject_email():
    assert (
        script.get_subject_email("/test_param/subject_email")
        == "subject_email@subjectemail.com"
    )


# @vcr.use_cassette
# def test_get_credentials_file():
#     actual_credentials_file = "./tests/test_files/test_credentials_file.json"
#     expected_credentials_file = "./tests/test_files/expected_credentials_file.json"

#     assert (
#         script.get_credentials_file(
#             "/test_param/credentials_file", actual_credentials_file
#         )
#         == actual_credentials_file
#     )
#     assert filecmp.cmp(actual_credentials_file, expected_credentials_file)


# @vcr.use_cassette
# def test_create_client():
#     api = "groupssettings"
#     api_version = "v1"
#     credentials_file = "./tests/test_files/test_credentials_file.json"
#     scope = "https://www.scope.test"
#     subject_email = "subject_email@email.com"
#     assert (
#         script.create_client(api, api_version, credentials_file, scope, subject_email)
#         == "client object"
#     )


@vcr.use_cassette
def test_build_group_dict():
    os.environ["CREDENTIALS"] = "/google_data_to_splunk/credentials"
    os.environ["SUBJECT"] = "/google_data_to_splunk/subject_email"
    os.environ["ADMIN_SCOPE"] = "/google_data_to_splunk/admin_readonly_scope"
    assert script.build_group_dict("admin", "directory_v1", "ADMIN_SCOPE")
