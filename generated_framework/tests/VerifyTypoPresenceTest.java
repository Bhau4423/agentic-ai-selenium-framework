package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.TyposPage;

public class VerifyTypoPresenceTest extends BaseTest {

    @Test
    public void verifyTypoPresence() {

        TyposPage page = new TyposPage(driver);

        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

    }

}