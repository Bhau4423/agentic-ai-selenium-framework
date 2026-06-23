package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.EntryAdPage;

public class AdLoadFailureTest extends BaseTest {

    @Test
    public void adLoadFailure() {

        EntryAdPage page = new EntryAdPage(driver);

        Assert.assertFalse(driver.getCurrentUrl().contains("dashboard"));

    }

}