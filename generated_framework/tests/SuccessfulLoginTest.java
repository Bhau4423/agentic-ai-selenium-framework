package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import pages.TestLoginPracticeTestAutomationPage;

public class SuccessfulLoginTest {

    @Test
    public void successfulLogin() {

        TestLoginPracticeTestAutomationPage page = new TestLoginPracticeTestAutomationPage(driver);

        page.get_password().sendKeys("TEST_DATA");
        page.get_button_0().sendKeys("TEST_DATA");

    }

}