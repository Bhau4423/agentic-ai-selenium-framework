package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.ForgotPasswordPage;

public class VerifyFormPresenceTest extends BaseTest {

    @Test
    public void verifyFormPresence() {

        ForgotPasswordPage page = new ForgotPasswordPage(driver);

        wait.until(ExpectedConditions.visibilityOf(page.get_email()));
        wait.until(ExpectedConditions.visibilityOf(page.get_Retrieve_password()));
        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

    }

}