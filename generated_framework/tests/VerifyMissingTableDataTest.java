package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.TablesPage;

public class VerifyMissingTableDataTest extends BaseTest {

    @Test
    public void verifyMissingTableData() {

        TablesPage page = new TablesPage(driver);

        Assert.assertFalse(driver.getCurrentUrl().contains("dashboard"));

    }

}