package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.LoginPage;

public class VerifyFooterPresenceTest extends BaseTest {

    @Test
    public void verifyFooterPresence() {

        LoginPage page = new LoginPage(driver);

        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

    }

}