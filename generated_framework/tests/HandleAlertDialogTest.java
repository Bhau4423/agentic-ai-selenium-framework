package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.JavascriptAlertsPage;

public class HandleAlertDialogTest extends BaseTest {

    @Test
    public void handleAlertDialog() {

        JavascriptAlertsPage page = new JavascriptAlertsPage(driver);

        wait.until(ExpectedConditions.visibilityOf(page.get_Click_for_JS_Alert()));
        // UNKNOWN ACTION : ALERT_ACCEPT

        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

    }

}