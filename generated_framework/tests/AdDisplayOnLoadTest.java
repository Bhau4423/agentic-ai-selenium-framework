package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.EntryAdPage;

public class AdDisplayOnLoadTest extends BaseTest {

    @Test
    public void adDisplayOnLoad() {

        EntryAdPage page = new EntryAdPage(driver);

        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

    }

}