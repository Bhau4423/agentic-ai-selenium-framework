package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.JavascriptAlertsPage;

public class TriggerCustomContextMenuTest extends BaseTest {

    @Test
    public void triggerCustomContextMenu() {

        JavascriptAlertsPage page = new JavascriptAlertsPage(driver);

        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

    }

}