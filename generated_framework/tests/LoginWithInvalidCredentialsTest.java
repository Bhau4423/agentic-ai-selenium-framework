package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.LoginPage;

public class LoginWithInvalidCredentialsTest extends BaseTest {

    @Test
    public void loginWithInvalidCredentials() {

        LoginPage page = new LoginPage(driver);

        wait.until(ExpectedConditions.visibilityOf(page.get_username()));
        page.get_username().sendKeys("TEST_DATA");

        wait.until(ExpectedConditions.visibilityOf(page.get_password()));
        page.get_password().sendKeys("TEST_DATA");


        Assert.assertFalse(driver.getCurrentUrl().contains("dashboard"));

    }

}