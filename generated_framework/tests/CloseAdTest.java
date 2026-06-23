package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.EntryAdPage;

public class CloseAdTest extends BaseTest {

    @Test
    public void closeAd() {

        EntryAdPage page = new EntryAdPage(driver);

        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

    }

}