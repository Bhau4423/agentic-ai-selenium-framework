package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.EntryAdPage;

public class VerifyNoCloseWithoutAdTest extends BaseTest {

    @Test
    public void verifyNoCloseWithoutAd() {

        EntryAdPage page = new EntryAdPage(driver);

        Assert.assertFalse(driver.getCurrentUrl().contains("dashboard"));

    }

}