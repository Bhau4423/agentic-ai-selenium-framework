package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.JavascriptAlertsPage;

public class TriggerDialogsWithoutInteractionTest extends BaseTest {

    @Test
    public void triggerDialogsWithoutInteraction() {

        JavascriptAlertsPage page = new JavascriptAlertsPage(driver);

        wait.until(ExpectedConditions.visibilityOf(page.get_Click_for_JS_Alert()));
        wait.until(ExpectedConditions.visibilityOf(page.get_Click_for_JS_Confirm()));
        wait.until(ExpectedConditions.visibilityOf(page.get_Click_for_JS_Prompt()));
        Assert.assertFalse(driver.getCurrentUrl().contains("dashboard"));

    }

}