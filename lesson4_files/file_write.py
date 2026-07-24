
with open("greeting.txt", "w", encoding = "utf-8") as file:
    file.write("Hello automated tests!\n")
    file.write("Second line")

def log_test_result(test_name, status):
    with open("test_run.log", "a", encoding = "utf-8") as log_file:
        log_file.write(f"{test_name}: {status}\n")

log_test_result("Test_login", "Passed")
log_test_result("Test_registration", "Failed")
log_test_result("Test_logout", "Passed")