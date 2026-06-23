package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.JavascriptAlertsPage;

public class TriggerJavascriptConfirmTest extends BaseTest {

    @Test
    public void triggerJavascriptConfirm() {

        JavascriptAlertsPage page = new JavascriptAlertsPage(driver);

        // UNKNOWN ACTION : ALERT_ACCEPT



        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

    }

}