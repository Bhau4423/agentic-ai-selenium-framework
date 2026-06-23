package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.AddRemoveElementsPage;

public class RemoveLastRemainingElementTest extends BaseTest {

    @Test
    public void removeLastRemainingElement() {

        AddRemoveElementsPage page = new AddRemoveElementsPage(driver);


        Assert.assertTrue(driver.getCurrentUrl().contains("dashboard"));

    }

}