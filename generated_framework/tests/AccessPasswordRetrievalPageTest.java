package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.LoginPage;

public class AccessPasswordRetrievalPageTest extends BaseTest {

    @Test
    public void accessPasswordRetrievalPage() {

        LoginPage page = new LoginPage(driver);

        wait.until(ExpectedConditions.visibilityOf(page.get_password()));
        page.get_password().sendKeys("TEST_DATA");

        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

    }

}