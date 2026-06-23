package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.ForgotPasswordPage;

public class SubmitPasswordRetrievalTest extends BaseTest {

    @Test
    public void submitPasswordRetrieval() {

        ForgotPasswordPage page = new ForgotPasswordPage(driver);

        wait.until(ExpectedConditions.visibilityOf(page.get_email()));
        page.get_email().sendKeys("TEST_DATA");

        wait.until(ExpectedConditions.visibilityOf(page.get_Retrieve_password()));
        page.get_Retrieve_password().sendKeys("TEST_DATA");

        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

    }

}