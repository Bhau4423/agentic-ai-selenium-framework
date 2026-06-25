package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.LoginPage;

public class SuccessfulLoginTest extends BaseTest {

    @Test
    public void successfulLogin() {

        LoginPage page = new LoginPage(driver);

        wait.until(ExpectedConditions.visibilityOf(page.get_username()));
        page.get_username().sendKeys("TEST_DATA");

        wait.until(ExpectedConditions.visibilityOf(page.get_password()));
        page.get_password().sendKeys("TEST_DATA");

        wait.until(ExpectedConditions.elementToBeClickable(page.get_Login()));
        page.get_Login().click();

        

        Assert.assertTrue(!driver.getCurrentUrl().isEmpty());

    }

}