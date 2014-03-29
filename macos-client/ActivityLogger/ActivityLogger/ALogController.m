//
//  ALogController.m
//  ActivityLogger
//
//  Created by David Arnold on 29/03/14.
//  Copyright (c) 2014 David Arnold. All rights reserved.
//

#import "ALogController.h"

@implementation ALogController
- (id)init
{
    self = [super init];
    if (self) {
        // Initialise here
    }
    
    printf("Controller got init.\n");
    
    // Try to start window as modal
    //[NSApp runModelForWindow];
    return self;
}


- (void)dealloc
{
    // this is flagged as an issue with ARC: [super dealloc];
}

- (IBAction)cancel:(id) sender
{
    printf("Controller got cancel.\n");
}

- (IBAction)ok:(id)sender
{
    printf("Controller got ok.\n");
    
    // Hide window
    //[taskWindow orderOut:self];
    
    char buf[200];
    [[comboBox stringValue] getCString:buf maxLength:200 encoding:NSASCIIStringEncoding];
    
    printf("Combo text: %s\n", buf);
}

@end
