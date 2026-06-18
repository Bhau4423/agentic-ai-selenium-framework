package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.TestLoginPage;

public class LoginWithInvalidEmailFormatTest extends BaseTest {

    @Test
    public void loginWithInvalidEmailFormat() {

        TestLoginPage page = new TestLoginPage(driver);

        wait.until(ExpectedConditions.visibilityOf(page.get_username()));
        page.get_username().sendKeys("TEST_DATA");

        wait.until(ExpectedConditions.visibilityOf(page.get_password()));
        page.get_password().sendKeys("TEST_DATA");

        wait.until(ExpectedConditions.elementToBeClickable(page.get_Submit()));
        page.get_Submit().click();

        wait.until(ExpectedConditions.visibilityOf(page.get_error_message()));
        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

        Assert.assertTrue(driver.getCurrentUrl().contains("dashboard"));

    }

}