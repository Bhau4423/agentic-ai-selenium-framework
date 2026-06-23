package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.JavascriptAlertsPage;

public class RapidDialogTriggeringTest extends BaseTest {

    @Test
    public void rapidDialogTriggering() {

        JavascriptAlertsPage page = new JavascriptAlertsPage(driver);

        // UNKNOWN ACTION : ALERT_ACCEPT



        Assert.assertTrue(driver.getCurrentUrl().contains("dashboard"));

    }

}