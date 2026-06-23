package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.JavascriptAlertsPage;

public class TriggerAlertWithoutInteractionTest extends BaseTest {

    @Test
    public void triggerAlertWithoutInteraction() {

        JavascriptAlertsPage page = new JavascriptAlertsPage(driver);

        wait.until(ExpectedConditions.visibilityOf(page.get_Click_for_JS_Alert()));
        // UNKNOWN ACTION : ALERT_ACCEPT

        Assert.assertFalse(driver.getCurrentUrl().contains("dashboard"));

    }

}