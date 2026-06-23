package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.JavascriptAlertsPage;

public class HandleJavascriptConfirmTest extends BaseTest {

    @Test
    public void handleJavascriptConfirm() {

        JavascriptAlertsPage page = new JavascriptAlertsPage(driver);

        wait.until(ExpectedConditions.visibilityOf(page.get_Click_for_JS_Alert()));
        // UNKNOWN ACTION : ALERT_ACCEPT

        wait.until(ExpectedConditions.elementToBeClickable(page.get_Click_for_JS_Confirm()));
        page.get_Click_for_JS_Confirm().click();

        wait.until(ExpectedConditions.elementToBeClickable(page.get_Click_for_JS_Prompt()));
        page.get_Click_for_JS_Prompt().click();

        Assert.assertTrue(driver.getCurrentUrl().length() > 0);

    }

}