package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.LoginPage;

public class SuccessfulLogoutTest extends BaseTest {

    @Test
    public void successfulLogout() {

        LoginPage page = new LoginPage(driver);

        // wait.until(ExpectedConditions.elementToBeClickable(page.get_Login()));
        wait.until(ExpectedConditions.elementToBeClickable(page.get_Login()));
        page.get_Login().click();

        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

    }

}