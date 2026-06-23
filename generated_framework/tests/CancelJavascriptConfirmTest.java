package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.JavascriptAlertsPage;

public class CancelJavascriptConfirmTest extends BaseTest {

    @Test
    public void cancelJavascriptConfirm() {

        JavascriptAlertsPage page = new JavascriptAlertsPage(driver);

        // UNKNOWN ACTION : ALERT_ACCEPT



        Assert.assertFalse(driver.getCurrentUrl().contains("dashboard"));

    }

}