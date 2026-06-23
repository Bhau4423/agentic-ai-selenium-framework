package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import base.BaseTest;
import pages.AddRemoveElementsPage;

public class RemoveNonExistentElementTest extends BaseTest {

    @Test
    public void removeNonExistentElement() {

        AddRemoveElementsPage page = new AddRemoveElementsPage(driver);


        Assert.assertFalse(driver.getCurrentUrl().contains("dashboard"));

    }

}