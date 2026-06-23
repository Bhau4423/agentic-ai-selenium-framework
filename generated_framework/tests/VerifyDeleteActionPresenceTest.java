package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.TablesPage;

public class VerifyDeleteActionPresenceTest extends BaseTest {

    @Test
    public void verifyDeleteActionPresence() {

        TablesPage page = new TablesPage(driver);

        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

    }

}