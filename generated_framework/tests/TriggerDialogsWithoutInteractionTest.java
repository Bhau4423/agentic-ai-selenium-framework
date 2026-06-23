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

        Assert.assertFalse(driver.getCurrentUrl().contains("dashboard"));

    }

}