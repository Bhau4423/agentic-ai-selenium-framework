package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.TablesPage;

public class VerifyNoActionExecutionTest extends BaseTest {

    @Test
    public void verifyNoActionExecution() {

        TablesPage page = new TablesPage(driver);

        Assert.assertFalse(driver.getCurrentUrl().contains("dashboard"));

    }

}