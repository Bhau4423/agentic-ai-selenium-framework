package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.ForgotPasswordPage;

public class VerifyPasswordFormPresenceTest extends BaseTest {

    @Test
    public void verifyPasswordFormPresence() {

        ForgotPasswordPage page = new ForgotPasswordPage(driver);

        // wait.until(ExpectedConditions.visibilityOf(page.get_password()));
        wait.until(ExpectedConditions.elementToBeClickable(page.get_password()));
        page.get_password().sendKeys("TEST_DATA");

        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

    }

}